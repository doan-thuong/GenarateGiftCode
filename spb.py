from service import SupabaseService as spbS
import os

# name_table = "blacklist_device"
# col = "device_or_uid"
name_table = "mail_box"
col = "player_id"
# name_table = "daily_challenge_ticket"
# col = "uid"
# name_table = "daily_challenge_weekly_pack"
# col = "uid"
# name_table = "player_info"
# col = "device_id"
condition = "q3PgSFzDqTPbtvT3LvsD3XyOjSS2"

# list_col_need_to_get = ["uid","rank","last_ranking_top"]

res = spbS.read_data_from_table_with_filter(name_table, col, condition)

os.system('cls')

print(f"Len: {len(res)}")
print("---------------------------")

for item in res:
    for k, v in item.items():
        
        print(f"{k}: {v}")
    # break
    print("---------------------------")

# for item in res:
#     for k, v in item.items():
#         if k in list_col_need_to_get:
#             print(f"{k}: {v}")
#     print("---------------------------")

# for i in range(50):
#     for k,v in res[i].items():
#         print(f"{k}: {v}")
#     print("---------------------------")