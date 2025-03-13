import os
import shutil

def copy_static_to_public(static_path, public_path):
        if os.path.exists(public_path):
                shutil.rmtree(public_path)
        os.mkdir(public_path)
        copy_recursive(static_path, public_path)
        


def copy_recursive(static_path, public_path):
        for item in os.listdir(static_path):
                item_path = os.path.join(static_path, item)
                new_item_path = os.path.join(public_path, item)
                if os.path.isfile(item_path):
                        shutil.copy(item_path, new_item_path)
                elif os.path.isdir(item_path):
                        os.mkdir(new_item_path)
                        copy_recursive(item_path, new_item_path)
    
public_path = "/home/odin/workspace/github.com/GirafficCorn/StaticSite/public"
static_path = "/home/odin/workspace/github.com/GirafficCorn/StaticSite/static"
    
copy_static_to_public(static_path, public_path)