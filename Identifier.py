import cv2


class Identifier:

    def __init__(self):
        self._root_dir: str = "/Users/kealenpillay/Documents/Projects/assignment-1/Object_Detection_Files/"
        self._class_file: str = self._root_dir + "coco.names"
        self._config_path: str = self._root_dir + "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
        self._weights_path: str = self._root_dir + "frozen_inference_graph.pb"
        self.class_names: list[str] = []
        self.animals: dict[int, str] = {
            16: "bird",
            17: "cat",
            18: "dog",
            19: "horse",
            20: "sheep",
            21: "cow",
            22: "elephant",
            23: "bear",
            24: "zebra",
            25: "giraffe",
        }
        self.net = cv2.dnn_DetectionModel(self._weights_path, self._config_path)
        self.model_input_config()

    def load_class_names(self):
        with open(self._class_file, "rt") as f:
            self.class_names = f.read().rstrip("\n").split("\n")

    def model_input_config(self):
        self.net.setInputSize(320, 320)
        self.net.setInputScale(1.0 / 127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwapRB(True)
        self.load_class_names()
