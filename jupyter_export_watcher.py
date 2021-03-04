from pathlib import Path
import os

dirs = set()
for path in Path().rglob("*.ipynb"):
    path = str(path)
    if ".ipynb_checkpoints" not in path:
        dirs.add("/".join(path.split("\\")[:-1]))

for dir_ in dirs:
    command = "jupyter nbconvert --to script ./{}/*.ipynb".format(dir_)
    os.system(command)

print("...Removing whitespace from names...")
for path in Path().rglob("*.py"):
    path = str(path)
    if ".ipynb_checkpoints" not in path:
        split_path = path.split("\\")
        dir_, fname = "/".join(split_path[:-1]), split_path[-1]
        if " " in fname:
            without_ws_fname = "".join(fname.split())
            os.rename("./"+path, "./"+dir_+"/"+without_ws_fname)
