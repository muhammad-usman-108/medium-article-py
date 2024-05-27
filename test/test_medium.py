import unittest
from src.medium import MediumArticles

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.medium_articles = MediumArticles()
        self.username = "@engrmuhammadusman108"

    def test_get_profile_url(self):
        result = self.medium_articles.get_profile_url(self.username)
        self.assertEqual(result, 'https://medium.com/feed/@engrmuhammadusman108')

if __name__ == '__main__':
    unittest.main()