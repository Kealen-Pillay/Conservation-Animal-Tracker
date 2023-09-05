from WikipediaInstanceFactory import WikipediaInstanceFactory
from wikipediaapi import Wikipedia, WikipediaPage


class WikipediaScraper:
    def __init__(self, language: str = "en") -> None:
        self._user_agent: str = "Animal_Descriptor (wkm9223@autuni.ac.nz)"
        self._language: str = language
        self.content = {"current_page": "", "summary": "", "history": []}

    def scrape(self, target_page: str) -> None:
        wiki_wiki: Wikipedia = WikipediaInstanceFactory.create_wikipedia_instance(
            user_agent=self._user_agent,
            language=self._language
        )
        page: WikipediaPage = wiki_wiki.page(target_page)
        if not page.exists():
            self.content["summary"] = "THIS PAGE DOES NOT EXIST!"
        else:
            self.content["current_page"] = page.title
            self.content["summary"] = page.summary
            self.content["history"].append(page.title)

    def display_page(self) -> None:
        print(self.content["current_page"])
        underline: str = "=" * len(self.content["current_page"])
        print(underline)
        print(self.content["summary"])
