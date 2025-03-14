from block import *
from htmlnode import *
from markdown import *
from texttotextnodes import *
from textnode import *
from parentnode import *

def markdown_to_blocks(markdown):
    prep = markdown.strip()
    base = prep.split("\n\n")
    return base


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_nodes = []
    for block in blocks:
        new_nodes.append(block_to_html_node(block))
    return ParentNode("div", new_nodes)

#Create an html node from a block
def block_to_html_node(block):
    type = block_to_block_type(block)
    children = text_to_children(block)
   
    if type == BlockTypes.PARAGRAPH:
        text = block.replace("\n", " ")
        children = text_to_children(text)
        return ParentNode("p", children)
    elif type == BlockTypes.HEADING:
        count = 0
        for i in range(0, 6):
            if block[i] == "#":
                count += 1
        text = block.replace("#", "")
        text = text.strip()
        children = text_to_children(text)
        return ParentNode(f"h{count}", children)
    elif type == BlockTypes.QUOTE:
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            if not line.startswith(">"):
                raise ValueError("invalid quote block")
            new_lines.append(line.lstrip(">").strip())
        content = " ".join(new_lines)
        children = text_to_children(content)
        return ParentNode("blockquote", children)
    elif type == BlockTypes.UNORDERED_LIST:
        text1 = block.replace("- ", "<li>")
        text2 = text1.replace("\n", "</li>")
        children = text_to_children(text2)
        return ParentNode("ul", children)
    elif type == BlockTypes.ORDERED_LIST:
        items = []
        text2 = block.split("\n")
        
        for line in text2:
            slice = line[3:]
            children = text_to_children(slice)
            items.append(ParentNode("li", children))
        return ParentNode("ol", items)
    elif type == BlockTypes.CODE:
        text = block.strip()
        text = block[3:-3].replace("\n", "\\n")
        # Create text node with raw content
        text_node = TextNode(text, TextType.TEXT)
        code_node = ParentNode("code", [text_node.text_node_to_html_node()])
        # Wrap in pre tag
        return ParentNode("pre", [code_node])
    




    

def text_to_children(text):
    new_nodes = []
    #Generate text nodes from text
    text_nodes = text_to_textnodes(text)
    #Generate leaf nodes from text nodes
    for node in text_nodes:
        new_nodes.append(node.text_node_to_html_node())
    return new_nodes


