import os
import shutil

def copy_static_to_public(static_path, public_path):
        if not os.path.exists(public_path):
                os.mkdir(public_path)
        for item in os.listdir(static_path):
                item_path = os.path.join(static_path, item)
                new_item_path = os.path.join(public_path, item)
                if os.path.isfile(item_path):
                        shutil.copy(item_path, new_item_path)
                else: 
                        copy_static_to_public(item_path, new_item_path)

