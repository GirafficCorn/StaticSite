from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
import os
import shutil
from extracttitle import *
from copystatictopublic import *
from markdowntoblock import *
from generatepagesrecursively import *
import sys

'''def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        file_content = f.read()
    with open(template_path, 'r') as t:
        temp_content = t.read()

    node = markdown_to_html_node(file_content)
    html = node.to_html()

    title = extract_title(file_content)
    temp_content = temp_content.replace("{{ Title }}", title)
    temp_content = temp_content.replace("{{ Content }}", html)
    

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    filepath = open(dest_path, "w")
    filepath.write(temp_content)'''


    
    


path_static = "./static"
path_public = "./docs"
path_content = "./content"
template_path = "./template.html"
basepath = sys.argv

def main():
   if os.path.exists(path_public):
    shutil.rmtree(path_public)
   
    copy_static_to_public(path_static, path_public)
 
    #generate_page(os.path.join(path_content, "index.md"), template_path, os.path.join(path_public, "index.html"))
    generate_pages_recursive(path_content, template_path, path_public, basepath)
    

    

main()