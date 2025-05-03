import string
import random
import os
import json

def gen_random_string(length=9):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))

def check_duplicate(str, listStr):
    for item in listStr:
        if item == str:
            return False
        
    return True

def delete_element_in_file_json(codes_to_delete):
    with open("file.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data = [item for item in data if list(item.keys())[0] not in codes_to_delete]

    with open("file.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def append_json_to_file(file_path, data_append):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("data in file json error")
                data = []
    else:
        data = []
        print("file json not found")
    
    if isinstance(data_append, list):
        data.extend(data_append)
    else:
        data.append(data_append)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)