from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.props = props
        

    def to_html(self):
        if not self:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            if self.tag == "a":
                return f"<a{self.props_to_html()}>{self.value}</a>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

