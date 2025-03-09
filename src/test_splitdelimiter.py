import unittest
from splitdelimiter import *


class TestSplitDelimiter(unittest.TestCase):
    def test_split_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [TextNode("This is text with a ", TextType.TEXT, None),
                          TextNode("code block", TextType.CODE, None),
                          TextNode(" word", TextType.TEXT, None)
                          ]
                          )

    def test_split_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, 
                         [TextNode("This is text with a ", TextType.TEXT, None),
                          TextNode("bold", TextType.BOLD, None),
                          TextNode(" word", TextType.TEXT, None)
                          ]
                          )
        
    def test_split_delimiter(self):
        self.assertRaises(Exception, split_nodes_delimiter, 
                          TextNode("This is text with a **bold** word", TextType.TEXT),
                          "`",
                          TextType.BOLD
                          )


if __name__ == "__main__":
    unittest.main()


