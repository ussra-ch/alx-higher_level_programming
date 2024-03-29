#!/usr/bin/python3
"""script writes an Object to a text file, using a JSON representation."""
import json

def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
