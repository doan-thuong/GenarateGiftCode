from supabase import create_client, Client

import config.SupabaseConfig as SupabaseConfig
import config.ConfigMailSupabase as ConfigMailSupabase


def insert_mail(mail_id, create_at, title, des, status, reward_status, reward, player_id, table_name):
    path_url = "UrlSupabase.key"
    path_key = "KeySupabase.key"

    url = SupabaseConfig.get_url_supabase(path_url, False)
    key = SupabaseConfig.get_key_supabase(path_key, False)

    supabase: Client = create_client(url, key)

    data = ConfigMailSupabase.mail_box(mail_id, create_at, title, des, status, reward_status, reward, player_id)

    supabase.table(table_name).insert(data).execute()
