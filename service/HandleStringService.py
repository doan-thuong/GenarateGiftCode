import string
import random
import os
import json
from datetime import datetime
from cryptography.fernet import Fernet
from Crypto.Cipher import AES


BLOCK_SIZE = 16

def pad(data: str):
    padding_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + chr(padding_len) * padding_len

def gen_random_string(length=9):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choices(characters, k=length))

def unpad(data):
    padding_len = ord(data[-1])
    return data[:-padding_len]

def append_to_encrypted_json(input_path: str, password: str, new_data):
    with open(input_path, "rb") as f:
        encrypted_data = f.read()

    key = password.encode("utf-8")
    key = key[:16].ljust(16, b"0")

    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(encrypted_data)
    plain_text = unpad(decrypted.decode("utf-8"))

    try:
        json_data = json.loads(plain_text)
    except json.JSONDecodeError:
        json_data = []

    if isinstance(json_data, list):
        json_data.append(new_data)
    else:
        raise ValueError("JSON root is not a list, cannot append.")

    updated_json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
    padded_data = pad(updated_json_str)

    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(padded_data.encode("utf-8"))

    with open(input_path, "wb") as f:
        f.write(encrypted)

def print_log(data_write:list, action: str):
    case_log = {
        "call_update" : "Action call function update",
        "update" : "Action update",
        "call_delete" : "Action call function delete",
        "delete" : "Action delete",
    }
    data = {
        "log": f"[{datetime.now()}]: {case_log[action]} with data has len = {len(data_write)}.",
        "data": data_write
    }

    print(f"call print_log {action}")

    path_file = "D:/bvlvsdvdb/atad.json"
    encode_pw = "gAAAAABoWYkBYijM9A2FHsmSLMTq0tO6FieexaFYg2eZdbabgyjh3rrk4c6PnM89OYXbLStTZ4fwt9HAsmKqvMIKq8Ll0gjULA=="
    pw = decrypt_password(encode_pw)

    append_to_encrypted_json(path_file, pw, data)

def decrypt_password(encrypted_password: str) -> str:
    path = "D:/nvaivaos/yek.txt"
    with open(path, "rb") as key_file:
        saved_key = key_file.read()
    
    cipher_suite = Fernet(saved_key)

    decrypted_password = cipher_suite.decrypt(encrypted_password.encode())

    return decrypted_password.decode()

def check_duplicate(str, listStr):
    for item in listStr:
        if item == str:
            return False
        
    return True

def delete_element_in_file_json(codes_to_delete, path_file):
    with open(path_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    data = [item for item in data if list(item.keys())[0] not in codes_to_delete]

    with open(path_file, "w", encoding="utf-8") as f:
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

def write_data(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)