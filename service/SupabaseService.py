from supabase import create_client, Client

import config.SupabaseConfig as SupabaseConfig
import config.ConfigTableSupabase as ConfigTableSupabase

path_url = "UrlSupabase.key"
path_key = "KeySupabase.key"

url = SupabaseConfig.get_url_supabase(path_url, False)
key = SupabaseConfig.get_key_supabase(path_key, False)

if url is None or key is None:
    raise ValueError("Supabase URL or Key is missing!")

supabase: Client = create_client(url, key)

def insert_mail(mail_id, create_at, title, des, status, reward_status, reward, player_id, bonus_percent, table_name):
    data = ConfigTableSupabase.mail_box(mail_id, create_at, title, des, status, reward_status, reward, player_id, bonus_percent)

    try:
        res = supabase.table(table_name).insert(data).execute()
        
        return res
    except Exception as e:
        print("Insert fail")
        print("Chi tiết lỗi:", e)
        
        return None
    
def insert_white_list(device_id, name, device_type):
    data = ConfigTableSupabase.whitelist_device(device_id, name, device_type)

    try:
        res = supabase.table("whitelist_device").insert(data).execute()
        
        return res
    except Exception as e:
        print("Insert fail")
        print("Chi tiết lỗi:", e)

def read_data_from_table(name_table):
    response = supabase.table(name_table).select("*").execute()

    return response.data

def read_data_from_table_with_sort(name_table, col, desc=False):
    try:
        response = supabase.table(name_table).select("*").order(col, desc=desc).execute()

        return response.data
    except Exception as e:
        print("Chi tiết lỗi:", e)
        return []

def read_data_from_table_with_filter(name_table, col, condition):
    if not col and not condition:
        response = supabase.table(name_table).select("*").execute()
    else:
        response = supabase.table(name_table).select("*").eq(col, condition).execute()

    return response.data

def read_data_by_ilike_col(name_table, col, search_string: str):
    response = supabase.table(name_table) \
        .select("*") \
        .ilike(col, f"{search_string}%") \
        .execute()
    
    return response