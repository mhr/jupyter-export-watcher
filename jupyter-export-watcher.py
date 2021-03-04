from pathlib import Path
import os
import shutil

dirs = set()
for path in Path().rglob("*.ipynb"):
    path = str(path)
    path = path.replace("\\", "/") # switch from Windows-style to Unix
    if ".ipynb_checkpoints" not in path:
        dirs.add("/".join(path.split("/")[:-1]))

for dir_ in dirs:
    command = "jupyter nbconvert --to script ./{}/*.ipynb".format(dir_)
    os.system(command)

print("...Removing whitespace from *.py names...")
for path in Path().rglob("*.py"):
    path = str(path)
    path = path.replace("\\", "/") # switch from Windows-style to Unix
    if ".ipynb_checkpoints" not in path and "jupyter-export-watcher" not in path:
        split_path = path.split("/")
        dir_, fname = "/".join(split_path[:-1]), split_path[-1]
        if " " in fname:
            without_ws_fname = "".join(fname.split())
            shutil.move("./"+path, "./"+dir_+"/"+without_ws_fname)
