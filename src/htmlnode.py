
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value
        
        children_html = ""
        if self.children:
            for child in self.children:
                children_html += child.to_html()
        
        props_html = self.props_to_html() if hasattr(self, "props_to_html") and self.props else ""

        if self.children:
            return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

        
    def props_to_html(self):
        conversions = []
        for k, v in self.props.items():
            conversions.append(f" {k}=\"{v}\"")
        return " ".join(conversions)

    def __repr__(self):
        return f"HMTLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, HTMLNode1):
        if HTMLNode1.tag == self.tag and HTMLNode1.value == self.value and HTMLNode1.children == self.children and HTMLNode1.props == self.props:
            return True
        return False
    