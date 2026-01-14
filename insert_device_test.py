from service import SupabaseService as spbS
from config import Enum


def add_cheat():
    device_id = "F11E183F-1490-4DE9-B931-93638962B7CF"
    name = "thg ios 1"
    device_type = Enum.DeviceType.InHouse

    res = spbS.insert_white_list(device_id, name, device_type)

    if res:
        print("success")

def ban_acc():
    infor = "aBIOfzXuq3bc8valhJRSOhdCXmV2"
    reason = "cheat lv item"

    res = spbS.insert_black_list(infor, reason)

    if res:
        print("success")

if __name__ == "__main__":
    # add_cheat()
    ban_acc()