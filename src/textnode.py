from enum import Enum

class TextType(Enum):
    NORMAL = "Normal text"
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
