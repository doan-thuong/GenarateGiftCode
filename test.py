import service.FireBaseService as auto
import service.HandleStringService as handleStr
import service.GiftCodeService as gcService
import service.FireBaseService as fbService
import json


# with open("OutPutGenerateCode.json", "r", encoding="utf-8") as f:
#     data = json.load(f)

# list_gc = ["BcIOqui7Q"]

# for item in data:
#     for key, value in item.items():
#         packs = value["packs"]
    
#         for pack in packs:
#             pack_id = pack["packId"]
#             pack_type = pack["packType"]
            
#             if(pack_id == 5 and pack_type == 22):
#                 list_gc.append(key)
#                 break

# if list_gc:
#     auto.delete_gift_code(list_gc)
    # handleStr.delete_element_in_file_json(list_gc, "OutPutGenerateCode.json")

response = [
    {"DISCORD5000": "1-0-2000-0-0"},
    {"DISCORD10000": "8-0-10-0-0"},
    {"NIGHTFALL15K": "8-0-20-0-0"},
    {"SANTAFALL24": "8-0-20-0-0"},
    {"NIGHTFALL8888": "8-0-10-0-0"},
    {"WELCOME2025": "8-0-20-0-0\n10-0-20-0-0"},
]

list_gift_code = []
for item in response:
    for key, value in item.items():
        reward_split_dash = gcService.handle_reward_in_gift_code(value)
        rewards = gcService.handle_reward(reward_split_dash)

        gen_code = fbService.res_gift_code_all(key, [], rewards)

        gcode = {key: gen_code}

        list_gift_code.append(gcode)

fbService.update_gift_code(list_gift_code)