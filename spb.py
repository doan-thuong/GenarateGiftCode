from service import SupabaseService as spbS
import os

# name_table = "blacklist_device"
# col = "device_or_uid"

# name_table = "whitelist_device"
# col = "device_id"

# name_table = "mail_box"
# col = "player_id"

# name_table = "daily_challenge_ticket"
# col = "uid"
# name_table = "daily_challenge_weekly_pack"

name_table = "guild"
col = "exp"

# col = "uid"
# name_table = "player_info"
# col = "device_id"

# condition = "BJhF8AvLyeQ8fRXeDNplGjaPr1r2"

# list_col_need_to_get = ["uid","rank","last_ranking_top"]

# res = spbS.read_data_from_table_with_filter(name_table, col, condition)
res = spbS.read_data_from_table_with_sort(name_table, col, True)

os.system('cls')

print(f"Len: {len(res)}")
print("---------------------------")

# i = 0

for item in res:
    # if i > 5: break
    
    for k, v in item.items():
        
        print(f"{k}: {v}")
    # break
    print("---------------------------")
    # i += 1

# for item in res:
#     for k, v in item.items():
#         if k in list_col_need_to_get:
#             print(f"{k}: {v}")
#     print("---------------------------")

# for i in range(50):
#     for k,v in res[i].items():
#         print(f"{k}: {v}")
#     print("---------------------------")