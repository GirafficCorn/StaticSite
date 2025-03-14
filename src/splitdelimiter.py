
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or delimiter not in node.text:
            new_nodes.append(node)
            continue
        else:
            #Represent object as a string, then split it
            working_list = node.text.split(delimiter)
          
            #Create new TextNode for each string block
            for chunk in working_list:
                if chunk == working_list[0] or chunk == working_list[-1]:
                    new_nodes.append(TextNode(chunk, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(chunk, text_type))
    return new_nodes






