from enum import Enum
from leafnode import *


class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode1):
        if TextNode1.text == self.text and TextNode1.text_type == self.text_type and TextNode1.url == self.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": f"{self.url}"})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": f"{self.url}", "alt": f"{self.text}"})
        raise Exception




