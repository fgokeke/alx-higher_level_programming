#!/usr/bin/python3
""" a script that adds all arguments to a Python list,
and then save them to a file"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items_list = []
    args = sys.argv[1:]
    items_list.extend(args)
    save_to_json_file(items_list, "add_item.json")
