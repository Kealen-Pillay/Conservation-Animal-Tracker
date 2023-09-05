import wikipediaapi
from wikipediaapi import Wikipedia


class WikipediaInstanceFactory:
    @staticmethod
    def create_wikipedia_instance(user_agent: str, language: str = "en") -> Wikipedia:
        return wikipediaapi.Wikipedia(user_agent=user_agent, language=language)
