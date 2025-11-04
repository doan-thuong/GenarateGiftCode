from service import SupabaseService as spbS

name_table = "guild_member"
col = "member_id"
while True:
    pre_uid = input("pre_uid or 'exit': ").strip()
    if pre_uid.lower() == "exit":
        print("Kết thúc chương trình.")
        break

    later_uid = input("Nhập chuỗi kết thúc (later_uid): ").strip()

    res = spbS.read_data_by_ilike_col(name_table, col, pre_uid)

    matched = [
        item for item in res.data
        if item["member_id"].startswith(pre_uid) and item["member_id"].endswith(later_uid)
    ]

    if matched:
        for item in matched:
            print(item["member_id"])
    else:
        print(f"Không tìm thấy member_id nào bắt đầu bằng '{pre_uid}' và kết thúc bằng '{later_uid}'")