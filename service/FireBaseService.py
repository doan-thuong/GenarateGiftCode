from typing import Any
from google.cloud.firestore_v1 import DELETE_FIELD

from config import FireBaseConfig as fbConfig
import service.HandleStringService as strService

DOC_REF = fbConfig.get_fire_base()

def read_gift_codes():
    try:
        doc = DOC_REF.get()

        codes = []

        if not doc.exists:
            print("Not found gift_code")
            return {}

        data: dict[str, Any] = doc.to_dict() or {}
        gift_codes = data.get("giftCodes", {})

        if len(gift_codes) == 0:
            print("Gift code null!")

        for code in gift_codes:
            codes.append(code)

        return codes
    except Exception as e:
        print(f'Error reading gift codes: {e}')
        return {}

def create_gift_code(deviceId, packs, rewards, type = 1):
    doc = DOC_REF.get()

    list_code = read_gift_codes()

    if not doc.exists:
        print("Not found gift_code")
        return {}

    render_code = strService.gen_random_string()

    while not strService.check_duplicate(render_code, list_code):
        render_code = strService.gen_random_string()
    
    return {
        render_code: get_gift_code_data(render_code, deviceId, packs, rewards, type = type)
    }

def update_gift_code(giftCodes):
    # strService.print_log(giftCodes, "call_update")

    # is_update = False

    for gift_code in giftCodes:
        for code, data in gift_code.items():
            DOC_REF.update({
                f"giftCodes.{code}": data
            })
            # is_update = True

    # if is_update:
        # strService.print_log(giftCodes, "update")

def delete_gift_code(gift_codes_to_delete):
    # strService.print_log(gift_codes_to_delete, "call_delete")

    if not gift_codes_to_delete:
        return

    delete = {f"giftCodes.{code}": DELETE_FIELD for code in gift_codes_to_delete}
    DOC_REF.update(delete)
    # strService.print_log(gift_codes_to_delete, "delete")
    print("Deleted!")

def get_gift_code_data(code, deviceId, packs, rewards, type = 1):
    gift_code_data = {
        "code": code,
        "deviceId": deviceId,
        "giftCodeType": type,
        "packs": packs,
        "rewards": rewards
    }
    return gift_code_data

def res_gift_code_all(code, packs, rewards):
    gift_code_data = {
        "code": code,
        "deviceId": "",
        "giftCodeType": 0,
        "packs": packs,
        "rewards": rewards
    }
    return gift_code_data