import unittest
import functions

class TestStringFunctions(unittest.TestCase):

    def test_is_string(self):
        self.assertTrue(functions.is_string(""))
        self.assertFalse(functions.is_string("Python"))

    def test_reverse_string(self):
        self.assertEqual(functions.reverse_string("hello"), "olleh")
        self.assertEqual(functions.reverse_string("Python"), "nohtyP")
        self.assertEqual(functions.reverse_string("12345"), "54321")

    def test_is_palindrome(self):
        self.assertTrue(functions.is_palindrome("Тропа налево повела на порт"))
        self.assertTrue(functions.is_palindrome("race car"))
        self.assertFalse(functions.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(functions.count_vowels("оловянный"), 4)
        self.assertEqual(functions.count_vowels("Привет, Андрей"), 4)
        self.assertEqual(functions.count_vowels("aeiou"), 5)

    def test_remove_duplicates(self):
        self.assertEqual(functions.remove_first_occurrence("hello"), "helo")
        self.assertEqual(functions.remove_first_occurrence("Python"), "Python")
        self.assertEqual(functions.remove_first_occurrence("aabbcc"), "abc")

if __name__ == '__main__':
    unittest.main()