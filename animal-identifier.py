from queue import Queue
import cv2
from Identifier import Identifier
from Publisher import Publisher
from Consumer import Consumer

# Setup
identifier: Identifier = Identifier()
classification_buffer: Queue = Queue()
classified_animals: set[str] = set()
_sentinel = object
publisher: Publisher = Publisher(queue=classification_buffer,
                                 sentinel=_sentinel)
consumer: Consumer = Consumer(queue=classification_buffer,
                              sentinel=_sentinel)


# Identification function
def getObjects(img, thres, nms, draw=True, objects=[]):
    class_ids, confs, bbox = identifier.net.detect(img, confThreshold=thres, nmsThreshold=nms)

    if len(objects) == 0:
        objects = identifier.class_names
    object_info = []

    if len(class_ids) != 0:
        for classId, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):

            # Adding animals to queue
            if 16 <= classId <= 25:
                animal = identifier.animals[classId]
                publisher.add(animal)
                if animal not in classified_animals:
                    classified_animals.add(animal)
                    consumer.log_writer(animal)

            class_name = identifier.class_names[classId - 1]
            cv2.putText(
                img,
                "Press 'Q' to quit",
                (10, 30),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                1,
            )

            if class_name in objects:
                object_info.append([box, class_name])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(
                        img,
                        identifier.class_names[classId - 1].upper(),
                        (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (0, 255, 0),
                        2,
                    )

    return img, object_info


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    publisher.start()
    consumer.start()
    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(
            img=img,
            thres=0.65,
            nms=0.2,
            objects=[animal for animal in identifier.animals.values()],
        )

        cv2.imshow("Output", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            publisher.add_sentinel()
            publisher.join()
            consumer.join()
            break

    cap.release()
