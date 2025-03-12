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
    

        return HTMLNode("p", "", children)
    elif type == BlockTypes.HEADING:
        count = 0
        for i in range(0, 6):
            if block[i] == "#":
                count += 1
        text = block.replace("#", "")
        children = text_to_children(text)
        return HTMLNode(f"h{count}", None, children)
    elif type == BlockTypes.QUOTE:
        text = block.replace(">", "")
        children = text_to_children(text)
        return HTMLNode("blockquote", text, children)
    elif type == BlockTypes.UNORDERED_LIST:
        text1 = block.replace("- ", "<li>")
        text2 = text1.replace("\n", "</li>")
        children = text_to_children(text2)
        return HTMLNode("ul", None, children)
    elif type == BlockTypes.ORDERED_LIST:
        text1 = ""
        text2 = block.split("\n")
        for line in text2:
            slice = line[:3]
            text1 += (line.replace(slice, "<li>"))

        children = text_to_children(text1)
        return HTMLNode("ol", None, children)
    elif type == BlockTypes.CODE:
        text = block.strip()
        text = block[3:-3].replace("\n", "\\n")
        print("***", text)
        # Create text node with raw content
        text_node = TextNode(text, TextType.TEXT)
        print("***", text_node)
        code_node = HTMLNode("code", None, [text_node.text_node_to_html_node()])
        # Wrap in pre tag
        return HTMLNode("pre", None, [code_node])
    




    

def text_to_children(text):
    new_nodes = []
    #Generate text nodes from text
    text_nodes = text_to_textnodes(text)
    #Generate leaf nodes from text nodes
    for node in text_nodes:
        new_nodes.append(node.text_node_to_html_node())
    return new_nodes


