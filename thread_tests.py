import unittest
from queue import Queue
from Consumer import Consumer
from Publisher import Publisher


class ThreadTests(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()
        self._sentinel = object()
        self.publisher = Publisher(queue=self.queue,
                                   sentinel=self._sentinel)
        self.consumer = Consumer(queue=self.queue,
                                 sentinel=self._sentinel)

    def test_correct_sightings(self):
        self.publisher.start()
        self.consumer.start()
        self.publisher.add("horse")
        self.publisher.add("horse")
        self.publisher.add("horse")
        self.publisher.add_sentinel()
        self.publisher.join()
        self.consumer.join()
        self.assertEqual(3, self.consumer.sightings["horse"])

    def test_animals_sighted(self):
        self.publisher.start()
        self.consumer.start()
        self.publisher.add("horse")
        self.publisher.add("dog")
        self.publisher.add_sentinel()
        self.publisher.join()
        self.consumer.join()
        result = "horse" in self.consumer.animals_sighted and "dog" in self.consumer.animals_sighted
        self.assertTrue(result)

    def test_no_unintended_sighting_update(self):
        self.publisher.start()
        self.consumer.start()
        self.publisher.add("horse")
        self.publisher.add_sentinel()
        self.publisher.join()
        self.consumer.join()
        result = self.consumer.sightings["dog"] == 1
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
