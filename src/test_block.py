import unittest
from block import *

class TestBlock(unittest.TestCase):
    def test_header(self):
        test = block_to_block_type("##### Test")
        self.assertEqual(test, BlockTypes.HEADING)

    def test_code(self):
        test = block_to_block_type("```Test ```")
        self.assertAlmostEqual(test, BlockTypes.CODE)

    def test_quote(self):
        test = block_to_block_type(">Test\nTest\nTest")
        self.assertAlmostEqual(test, BlockTypes.QUOTE)

    def test_unordered_list(self):
        test = block_to_block_type("- Test\n- Test\n- Test")
        self.assertAlmostEqual(test, BlockTypes.UNORDERED_LIST)

    def test_ordered_list(self):
        test = block_to_block_type("1. Test\n2. Test\n3. Test")
        self.assertAlmostEqual(test, BlockTypes.ORDERED_LIST)
    



if __name__ == "__main__":
    unittest.main()