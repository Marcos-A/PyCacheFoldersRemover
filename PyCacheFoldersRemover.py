#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-

import os
import shutil
import sys

"""PyCacheFolderRemover 1.0
Deletes every "__pycache__" folder within the current dir from where this file is executed,
or from the directory passed as a parameter with its full path.
Use wisely. Remember "__pycache__" files (which will be either .pyc or .pyo files) will make your program start faster,
being recompiled every time your code is modified. "__pycache__" folders will reappear after every execution of your Python code.
"""

def remove_pycache_folders(dir_name):
    dirs_and_files = os.scandir(dir_name)
    for entry in dirs_and_files:
        if entry.is_dir():
            if os.path.basename(entry) == '__pycache__':
                shutil.rmtree(os.path.abspath(entry))
            else:
                remove_pycache_folders(entry)


if __name__ == "__main__":
    current_dir = os.getcwd()
    if (len(sys.argv) == 1):
        remove_pycache_folders(current_dir)
    elif (len(sys.argv) == 2):
        remove_pycache_folders(sys.argv[1])
