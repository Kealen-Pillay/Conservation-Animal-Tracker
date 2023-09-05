import os
import threading
from queue import Queue
from WikipediaScraperFactory import WikipediaScraperFactory


class Consumer(threading.Thread):

    def __init__(self, queue: Queue, sentinel):
        threading.Thread.__init__(self)
        self.thread_name = "Consumer"
        self._timeout = 2
        self._queue = queue
        self._sentinel = sentinel
        self.animals_sighted: set[str] = set()
        self.sightings: dict[str, int] = {
            "bird": 0,
            "cat": 0,
            "dog": 0,
            "horse": 0,
            "sheep": 0,
            "cow": 0,
            "elephant": 0,
            "bear": 0,
            "zebra": 0,
            "giraffe": 0
        }
        self.scraper = WikipediaScraperFactory.create_wikipediascraper_instance()

    def log_writer(self, animal: str) -> None:
        file = open(("logs/" + animal + ".txt"), "w")
        self.scraper.scrape(animal)
        file.write(f"{animal}\n")
        underline = "=" * len(animal)
        file.write(underline + "\n")
        file.write(self.scraper.content["summary"])
        file.close()

    def log_sightings(self) -> None:
        directory: str = "logs"
        instructions = "log_instructions.txt"
        for filename in os.listdir(directory):
            if filename != instructions:
                animal = filename.split(".")[0]
                f = open(directory + "/" + filename, "a")
                f.write(f"\nSightings: {self.sightings[animal]}")
                f.close()

    def run(self) -> None:
        while True:
            data = self._queue.get(timeout=None)
            if data is self._sentinel:
                print("Consumer terminating...")
                print("Logging Sightings")
                self.log_sightings()
                break
            else:
                self.animals_sighted.add(data)
                self.sightings[data] += 1
