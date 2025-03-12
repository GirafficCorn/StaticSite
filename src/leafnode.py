from htmlnode import *

#Leaf node is any end node that does not have any children
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
            if self.tag == "a" and self.props:
                return f"<a{self.props_to_html()}>{self.value}</a>"
            #if self.tag == "code":
                #return f"<pre><{self.tag}>{self.value}</{self.tag}></pre>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

