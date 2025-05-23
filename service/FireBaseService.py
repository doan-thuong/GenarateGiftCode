

from firebase_admin import firestore

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

def create_gift_code(deviceId, packs, rewards):
    doc = DOC_REF.get()

    list_code = read_gift_codes()

    if not doc.exists:
        print("Not found gift_code")
        return {}

    render_code = strService.gen_random_string()

    while not strService.check_duplicate(render_code, list_code):
        render_code = strService.gen_random_string()
    
    return {
        render_code: get_gift_code_data(render_code, deviceId, packs, rewards)
    }

def update_gift_code(giftCodes):
    for gift_code in giftCodes:
        for code, data in gift_code.items():
            DOC_REF.update({
                f"giftCodes.{code}": data
            })

def delete_gift_code(gift_codes_to_delete):
    delete = {f"giftCodes.{code}": firestore.DELETE_FIELD for code in gift_codes_to_delete}
    DOC_REF.update(delete)
    print("Deleted!")

def get_gift_code_data(code, deviceId, packs, rewards):
    gift_code_data = {
        "code": code,
        "deviceId": deviceId,
        "giftCodeType": 1,
        "packs": packs,
        "rewards": rewards
    }
    return gift_code_data