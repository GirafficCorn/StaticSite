from markdown import *
from textnode import *


def text_to_textnodes(text):
    results = []
    prepare = TextNode(text, TextType.TEXT)
    results.append(split_nodes_images(prepare))
    


text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

test = text_to_textnodes(text)

print(test)