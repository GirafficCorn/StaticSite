from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
import os
import shutil
from extracttitle import *
from copystatictopublic import *
from markdowntoblock import *

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        file_content = f.read()
    with open(template_path, 'r') as t:
        temp_content = t.read()

    node = markdown_to_html_node(file_content)
    html = node.to_html()
    title = extract_title(file_content)
    html_page = temp_content.replace("{{ Title }}", title)
    html_page = html_page.replace("{{ Content }}", html)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    filepath = os.path.join(dest_path, "index.html")
    with open(filepath, 'w') as file:
        file.write(html_page)

    
    
    #return html



def main():
    from_path = "/home/odin/workspace/github.com/GirafficCorn/StaticSite/content/index.md"
    template_path = "/home/odin/workspace/github.com/GirafficCorn/StaticSite/template.html"
    dest_path = "/home/odin/workspace/github.com/GirafficCorn/StaticSite/public/"        
    generate_page(from_path, template_path, dest_path)


    






main()