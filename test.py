import AutoCreateGiftCode as auto
import json


with open("OutPutGenerateCode.json", "r", encoding="utf-8") as f:
    data = json.load(f)

list_gc = [list(item.keys())[0] for item in data]

# auto.delete_gift_code(list_gc)