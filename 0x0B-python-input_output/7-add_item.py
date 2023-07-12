#!/usr/bin/python3
"""
load and save.
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    load and save
    """
    target_file = "add_item.json"
    if path.isfile(target_file):
        json_data = load_from_json_file(target_file)
    else:
        json_data = []
    for i in range(1, len(argv)):
        json_data.append(argv[i])
    save_to_json_file(json_data, target_file)


add_items()
