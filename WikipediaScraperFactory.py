from WikipediaScraper import WikipediaScraper


class WikipediaScraperFactory:
    @staticmethod
    def create_wikipediascraper_instance() -> WikipediaScraper:
        return WikipediaScraper(language="en")
