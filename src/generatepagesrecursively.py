import os
import shutil
from markdowntoblock import *
from extracttitle import *


   


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
 

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        new_item_path = os.path.join(dest_dir_path, item)
        if item_path.endswith(".md"):
            with open(template_path, "r") as t:
                template = t.read()
            with open(item_path, "r") as c:
                content = c.read()

            node = markdown_to_html_node(content)
            html = node.to_html()

            title = extract_title(os.path.join(content))
            
            

            template = template.replace("{{ Title }}", title)
            template = template.replace("{{ Content }}", html)
            template = template.replace(f"href=\"/", f"href=\"{basepath}")
            template = template.replace(f"src=\"/", f"src=\"{basepath}")
            dest_path = new_item_path.replace(".md", ".html")
            filepath = open(dest_path, "w")
            filepath.write(template)
            
        else:
            generate_pages_recursive(item_path, template_path, new_item_path, basepath)