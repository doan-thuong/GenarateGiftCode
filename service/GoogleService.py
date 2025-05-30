import gspread
import time
import os

from oauth2client.service_account import ServiceAccountCredentials


LINK_HEAD = "E:/project/security/"
COUNT = 0

def get_sheet(id_sheet, name_tab_sheet):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(LINK_HEAD + "config/key-gg-config.json", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(id_sheet)
    return spreadsheet.worksheet(name_tab_sheet)

def get_rows_by_columns_optimized(sheet, columns_to_get):
    all_values = sheet.get_all_values()
    headers = all_values[0]
    data_rows = all_values[1:]

    col_indexes = {}
    for col in columns_to_get:
        try:
            col_indexes[col] = headers.index(col)
        except ValueError:
            raise Exception(f"Không tìm thấy cột '{col}'")

    result = []
    for idx, row in enumerate(data_rows):
        row_number = idx + 2  # vì idx bắt đầu từ 0, dòng thực là từ 2
        row_data = {"row": row_number}
        empty = True

        for col_name, col_idx in col_indexes.items():
            value = row[col_idx] if col_idx < len(row) else ""
            if value.strip() != "":
                empty = False
            row_data[col_name] = value.strip()

        is_create = row_data.get("Is Create", "").strip()
        if not empty and is_create == "0":
            result.append(row_data)

    return result

def get_data_from_gg_sheet(id_sheet, name_tab_sheet):
  list_col = ["Device Id", "Pack", "Reward", "Is Create"]

  sheet = get_sheet(id_sheet, name_tab_sheet)
  data = get_rows_by_columns_optimized(sheet, list_col)

  if len(data) == 0:
    print("Data null")
    return None
  
  return data

def write_values_to_row_bulk(sheet, headers, row_number, data_dict):
    cells_to_update = []

    for col_name, value in data_dict.items():
        try:
            col_index = headers.index(col_name) + 1
            cell = gspread.Cell(row_number, col_index, value)
            cells_to_update.append(cell)
        except ValueError:
            print(f"Không tìm thấy cột '{col_name}' trong sheet.")

    if cells_to_update:
        sheet.update_cells(cells_to_update)

    global COUNT
    COUNT += 1
    print(f"{COUNT} time")
    time.sleep(0.5)

def get_dict_set_cell_sheet(code, is_check):
    return {
        "Trả lời/Phương án giải quyết (6)": "Gift code cho user: " + code,
        "Is Create" : is_check
    }