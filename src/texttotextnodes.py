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
    


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

test = text_to_textnodes(text)

for i in test:
    print(i)