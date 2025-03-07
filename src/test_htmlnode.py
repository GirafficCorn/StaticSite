import unittest
from htmlnode import*

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "This is test text", None, {"href": "htps://www.google.com", "target": "_blank"})
        test = node.props_to_html()
        correct = " href=\"https://www.google.com\" target=\"_blank\""
        if test == correct:
            return True
        return False
    
    def test_eq(self):
        node = HTMLNode("h1", "This is test text", None, {"href": "htps://www.google.com", "target": "_blank"})
        node2= HTMLNode("h1", "This is test text", None, {"href": "htps://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    
    def test_noteq(self):
        node = HTMLNode("h1", "This is test text", None, {"href": "htps://www.google.com", "target": "_blank"})
        node2= HTMLNode("h2", "test", None, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()