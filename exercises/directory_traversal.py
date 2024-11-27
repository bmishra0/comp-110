"""Traverse a directory structure recursively."""

from os import listdir
from os.path import join, isdir, getsize


def traverse(path: str) -> None:
    """Visit every file and directory in a directory."""
    print(f"Enter: {path}")
    children: list[str] = listdir(path)
    for child in children:
        if child[0] == "." or child[0] == "_":
            ...
        else:
            full_path: str = join(path, child)
            if isdir(full_path):
                traverse(full_path)
            else:
                print(f"{full_path} ({getsize(full_path)}))")
    print(f"Exit: {path}")


traverse(path="/workspace")
