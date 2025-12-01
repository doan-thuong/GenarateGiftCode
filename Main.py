import service.HandleStringService as strService
import service.GoogleService as gg
import service.GiftCodeService as gcService
import service.FireBaseService as fbService
import time


def main():
    id_sheet = "15f_OxWHC_OLuDryjyDBmD3WDN01DDuDYi573UuG3RVQ"
    tab_name = "Form Responses 1"

    sheet = gg.get_sheet(id_sheet, tab_name)
    headers = sheet.row_values(1)

    list_user = gg.get_data_from_gg_sheet(id_sheet, tab_name)

    if not list_user:
        return

    list_gift_code = []

    for user in list_user:
        device = user["Device Id"]

        # handle pack
        packs_from_user = user["Pack"]
        pack_split_dash = gcService.handle_pack_in_gift_code(packs_from_user)

        packs = gcService.handle_packs(pack_split_dash)

        # handle reward
        rewards_from_user = user["Reward"]
        reward_split_dash = gcService.handle_reward_in_gift_code(rewards_from_user)

        rewards = gcService.handle_reward(reward_split_dash)

        gen_code = fbService.create_gift_code(device, packs, rewards)
        list_gift_code.append(gen_code)

        # write data in gg sheet
        dict_data_cell = gg.get_dict_set_cell_sheet(list(gen_code.keys())[0], 1)
        row = user["row"]
        gg.write_values_to_row_bulk(sheet, headers, row, dict_data_cell)

    # Update gift code trên firebase
    fbService.update_gift_code(list_gift_code)

    # Write gift code vừa tạo vào file json để check
    strService.append_json_to_file("OutPutGenerateCode.json", list_gift_code)

    print("Done")

if __name__ == '__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Time run: {end - start:.4f}s")