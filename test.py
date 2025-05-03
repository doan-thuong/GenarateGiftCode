import AutoCreateGiftCode as auto
import HandleStringService as handleStr
import json


with open("OutPutGenerateCode.json", "r", encoding="utf-8") as f:
    data = json.load(f)

list_gc = []

for item in data:
    for key, value in item.items():
        packs = value["packs"]
    
        for pack in packs:
            pack_id = pack["packId"]
            pack_type = pack["packType"]
            
            if(pack_id == 5 and pack_type == 22):
                list_gc.append(key)
                break

if list_gc:
    auto.delete_gift_code(list_gc)
    handleStr.delete_element_in_file_json(list_gc, "OutPutGenerateCode.json")