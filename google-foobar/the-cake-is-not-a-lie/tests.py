import unittest
from solution import answer

class TestSolution(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(answer(""), 0)

    def test_none_type(self):
        self.assertEqual(answer(None), 0)

    def test_pattern_with_arity_2(self):
        self.assertEqual(answer("abccbaabccba"), 2)

    def test_pattern_with_arity_4(self):
        self.assertEqual(answer("abcabcabcabc"), 4)

    def test_no_pattern(self):
        self.assertEqual(answer("asdfghjkl"), 0)

if __name__ == '__main__':
    unittest.main()
