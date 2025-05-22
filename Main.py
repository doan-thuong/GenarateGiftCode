import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import service.HandleStringService as strService

import service.HandleStringService as strService
import service.GoogleService as gg

# Khởi tạo Firebase với file JSON credentials
service_account_path = "E:/Download/ezg-nightfall-firebase-adminsdk-.json"
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred)

# Kết nối tới Firestore
db = firestore.client()
doc_ref = db.collection("game_config").document("gift_code")

def create_gift_code(deviceId, packs):
    doc = doc_ref.get()

    list_code = read_gift_codes()

    if not doc.exists:
        print("Not found gift_code")
        return {}

    render_code = strService.gen_random_string()

    while not strService.check_duplicate(render_code, list_code):
        render_code = strService.gen_random_string()
    
    return {
        render_code: get_gift_code_data(render_code, deviceId, packs)
    }

def update_gift_code(giftCodes):
    for gift_code in giftCodes:
        for code, data in gift_code.items():
            doc_ref.update({
                f"giftCodes.{code}": data
            })

def read_gift_codes():
    try:
        doc = doc_ref.get()

        codes = []

        if not doc.exists:
            print("Not found gift_code")
            return {}

        data = doc.to_dict()
        gift_codes = data.get("giftCodes", {})

        if len(gift_codes) == 0:
            print("Gift code null!")

        for code in gift_codes:
            codes.append(code)

        return codes
    except Exception as e:
        print(f'Error reading gift codes: {e}')
        return {}

def delete_gift_code(gift_codes_to_delete):
    delete = {f"giftCodes.{code}": firestore.DELETE_FIELD for code in gift_codes_to_delete}
    doc_ref.update(delete)
    print("Deleted!")

def handle_packs(packs_old):
    packs_new = []

    for pack in packs_old:
        packs_new.append({
            "packId": int(pack[0]),
            "packType": int(pack[1])
        })
    
    return packs_new

def get_gift_code_data(code, deviceId, packs):
    gift_code_data = {
        "code": code,
        "deviceId": deviceId,
        "giftCodeType": 1,
        "packs": packs,
        "rewards": []
    }
    return gift_code_data

def get_dict_set_cell_sheet(code, is_check):
    return {
        "Trả lời/Phương án giải quyết (6)": "Gift code cho user: " + code,
        "Is Create" : is_check
    }

if __name__ == '__main__':
    id_sheet = "15f_OxWHC_OLuDryjyDBmD3WDN01DDuDYi573UuG3RVQ"
    tab_name = "Form Responses 1"

    list_user = gg.get_data_from_gg_sheet(id_sheet, tab_name)
    list_gift_code = []

    sheet = gg.get_sheet(id_sheet, tab_name)
    headers = sheet.row_values(1)

    for user in list_user:
        device = user.get("Device Id")
        
        pack_split_enter = list(map(str, user["Pack"].split("\n")))
        pack_split_dash = []

        for pack in pack_split_enter:
            pack_split_dash.append(pack.split("-"))

        packs = handle_packs(pack_split_dash)

        gen_code = create_gift_code(device, packs)
        list_gift_code.append(gen_code)

        dict_data_cell = get_dict_set_cell_sheet(list(gen_code.keys())[0], 1)
        row = user["row"]
        gg.write_values_to_row_bulk(sheet, headers, row, dict_data_cell)

    # Update gift code trên firebase
    update_gift_code(list_gift_code)

    # Write gift code vừa tạo vào file json để check
    strService.append_json_to_file("OutPutGenerateCode.json", list_gift_code)

    print("Done")