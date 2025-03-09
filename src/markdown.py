from textnode import *
import re

def extract_markdown_images(text):
    result = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def extract_markdown_links(text):
    result = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return result

def split_nodes_images(old_nodes):
    results = []
    #Iterate through each input node
    for node in old_nodes:
        base = node.text

        #Assign list of extracted images
        working = extract_markdown_images(base)
        
        #If there is no text, do not add anything to results
        if not base:
            return
        
        #If there are no images in the text, add the node as is to results
        if len(working) == 0:
            results.append(node)
        else:
            iter = 0
            while iter < len(working):
                temp = base.split(f"![{working[iter][0]}]({working[iter][1]})")
                results.append(TextNode(temp[0], TextType.TEXT))
                results.append(TextNode(working[iter][0], TextType.IMAGE, working[iter][1]))
                base = " ".join(temp[1:])
                iter += 1
            if base != "":
                results.append(TextNode(base, TextType.TEXT))

    return results


def split_nodes_link(old_nodes):
    results = []
    #Iterate through each input node
    for node in old_nodes:
        base = node.text

        #Assign list of extracted links
        working = extract_markdown_links(base)

        #If there is no text, do not add anything to results
        if not base:
            return
        
        #If there are no links in the text, add the node as is to results
        if len(working) == 0:
            results.append(node)
        else:
            iter = 0
            while iter < len(working):
                temp = base.split(f"[{working[iter][0]}]({working[iter][1]})")
                results.append(TextNode(temp[0], TextType.TEXT))
                results.append(TextNode(working[iter][0], TextType.LINK, working[iter][1]))
                base = " ".join(temp[1:])
                iter += 1
            if base != "":
                results.append(TextNode(base, TextType.TEXT))

    return results

