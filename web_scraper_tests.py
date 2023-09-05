import unittest
from WikipediaScraperFactory import WikipediaScraperFactory


class ScraperTests(unittest.TestCase):

    def setUp(self) -> None:
        self.scraper = WikipediaScraperFactory.create_wikipediascraper_instance()

    def test_correct_web_scrape(self):
        test_page = "horse"
        self.scraper.scrape(test_page)
        self.assertEqual("Horse", self.scraper.content["current_page"])

    def test_valid_web_scrape(self):
        test_page = "horse"
        self.scraper.scrape(test_page)
        result = self.scraper.content["summary"] == ""
        self.assertFalse(result)

    def test_invalid_web_scrape(self):
        test_page = "asfdsgfdg"
        self.scraper.scrape(test_page)
        result = self.scraper.content["summary"] == "THIS PAGE DOES NOT EXIST!"
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
