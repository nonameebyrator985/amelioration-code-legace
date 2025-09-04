import unittest
from utils import analyse_code, refactor_code


class TestUtils(unittest.TestCase):
    def test_analyse_code(self):
        code = 'print("test")'
        result = analyse_code(code)
        self.assertIn('problems', result)
        self.assertIn('suggestions', result)

    def test_refactor_code(self):
        code = 'print("test")'
        result = refactor_code(code)
        self.assertEqual(result, code)


if __name__ == '__main__':
    unittest.main()