from markdown import *
from textnode import *


def text_to_textnodes(text):
    base = [TextNode(text, TextType.TEXT)]
    base = split_nodes_images(base)
    #base = split_nodes_link([base])
    return base
    


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

test = text_to_textnodes(text)

print(test)