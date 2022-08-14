import unittest
import app
import validators

short_url = app.short_url

class TestShortening(unittest.TestCase):

    def test_shorten(self):
        self.assertEqual(len(short_url("http://google.com")), 4)
        self.assertEqual(short_url("http://google.com"), 'c7b9')
        self.assertEqual(type(short_url("http://google.com")), type("http://google.com"))

        # edge case-ek (üres string, naan, karakterek)

    def test_is_url(self):
        self.assertTrue(validators.url("http://google.com"))

        # működjön postmanből is, ne csak böngészőből (no forms!!!)
        # heroku élesítés
        # ütközés check
        # teszt: URL megy be??

if __name__ == '__main__':
    unittest.main()