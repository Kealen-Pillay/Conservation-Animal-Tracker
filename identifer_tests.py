import unittest

from Identifier import Identifier


class IdentifierTests(unittest.TestCase):

    def setUp(self) -> None:
        self.identifier = Identifier()

    def test_model_configured(self):
        self.assertTrue(self.identifier.net is not None)

    def test_class_names_loaded(self):
        result = True
        for animal in self.identifier.animals.values():
            if animal not in self.identifier.class_names:
                result = False
                break
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
