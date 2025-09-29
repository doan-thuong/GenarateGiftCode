from service import SupabaseService as spbS

name_table = "guild_member"
col = "member_id"
pre_uid = "djz"
later_uid = "982"

res = spbS.read_data_by_ilike_col(name_table, col, pre_uid)

matched = [
    item for item in res.data
    if item["member_id"].startswith(pre_uid) and item["member_id"].endswith(later_uid)
]

for item in matched:
    print(item["member_id"])