from htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props
        

    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag")
        if not self.children:
            raise ValueError("missing children")
        
        result = ""
        for i in self.children:
            #If object is parent node, it will call its own .to_html(). If it's a leaf node, it will call leaf nodes' to_html()
            result += i.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"