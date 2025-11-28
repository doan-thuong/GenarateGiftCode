import pandas as pd
import os

from service import SupabaseService as spbS

def print_data_to_excel(file_path, name_table):
    if not os.path.exists(file_path):
        print(f"File Excel chưa tồn tại")
        return
    
    res = spbS.read_data_from_table(name_table)

    try:
        df = pd.DataFrame(res)
        with pd.ExcelWriter(file_path, mode= "a", if_sheet_exists="replace", engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Sheet1")
    except Exception as e:
        print(f"Error when write data: {e}")

def print_data_to_console(name_table, col, condition):
    res = spbS.read_data_from_table_with_filter(name_table, col, condition)
    
    for item in res:
        for k, v in item.items():
            print(f"{k}: {v}")
        print("---------------------------")

# name_table = "daily_challenge_ranking"
# col = "uid"
name_table = "mail_box"
col = "player_id"
condition = "7aIsXviDEqcMKMogJZBQ4hM4WqT2"

print_data_to_console(name_table, col, condition)

# file_path = "D:/data_table.xlsx"
# print_data_to_excel(file_path, name_table)