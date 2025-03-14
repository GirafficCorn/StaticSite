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

def main():
    print("Starting site generation...")
    
    # Define paths
    path_static = "./static"
    path_public = "./docs"  # Use docs for GitHub Pages
    path_content = "./content"
    template_path = "./template.html"
    
    # Get basepath from command line arguments or default to "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    print(f"Using basepath: {basepath}")
    
    # Create or clean the output directory
    if os.path.exists(path_public):
        print(f"Cleaning {path_public} directory...")
        shutil.rmtree(path_public)
    
    print(f"Creating {path_public} directory...")
    os.makedirs(path_public)
    
    print("Copying static files...")
    copy_static_to_public(path_static, path_public)
    
    print("Generating pages...")
    generate_pages_recursive(path_content, template_path, path_public, basepath)
    
    print("Site generation complete!")

if __name__ == "__main__":
    main()