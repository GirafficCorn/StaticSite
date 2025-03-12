from markdown import *
from textnode import *
from splitdelimiter import *


def text_to_textnodes(text):
    base = [TextNode(text, TextType.TEXT)]
    base = split_nodes_images(base)
    base = split_nodes_link(base)
    base = split_nodes_delimiter(base, "**", TextType.BOLD)
    base = split_nodes_delimiter(base, "_", TextType.ITALIC)
    base = split_nodes_delimiter(base, "`", TextType.CODE)
    return base
    


