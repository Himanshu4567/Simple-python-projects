#!/usr/bin/python3

import os
import sys  
import time
red="\033[91m"
green="\033[92m"
blue="\033[94m"
End = '\033[0m' 

def content(dir_path,use_color=True):
    tree = []
    for root, dirs, files in os.walk(dir_path):
        level = root.replace(dir_path, '').count(os.sep)
        a = ' ' * 4 * (level)
        if use_color:
            tree.append(f"{a}{green}{os.path.basename(root)}{End}/")
        else:
            tree.append(f"{a}{os.path.basename(root)}/")
        b = ' ' * 4 * (level + 1)
        for f in files:
            if use_color:
                tree.append(f"{b}{blue}{f}{End}")
            else:
                tree.append(f"{b}{f}")
    return '\n'.join(tree)

def save_to(text, filename):
    with open(filename, 'w') as file:
        file.write(text)
        print(f"{red}\n------------------------------------------------------")
        print(f"[+] Directory tree saved to {filename}")
        print("------------------------------------------------------")


if len(sys.argv) > 1:
    start_time=time.time()
    directory_path = sys.argv[1] 
    if os.path.isdir(directory_path):
        tree_colored= content(directory_path,use_color=True)
        print(tree_colored)
        tree_plain=content(directory_path,use_color=False)
        save_to(tree_plain, "path.txt")
        end_time=time.time()
        print(f"Time Taken : {end_time - start_time: .2f} sec")
    else:
        print(f"{red}\n------------------------------------------------------")
        print("[+] The provided path does not exist or is not a directory.")
else:
    print("usage: path.py  <directory_path>")
