
LINK_PATH = "E:/project/security/"

def get_url_supabase(path, isInProject=True):
    url= None

    if not isInProject:
        path = LINK_PATH + path

    try:
        with open(path, "r") as file:
            url = file.read()
    except Exception as e:
        print(f"Lỗi đọc file url supabase: {e}")
    
    return url

def get_key_supabase(path, isInProject=True):
    key = None

    if not isInProject:
        path = LINK_PATH + path
    
    try:
        with open(path, "r") as file:
            key = file.read()
    except Exception as e:
        print(f"Lỗi đọc file key supabase: {e}")

    return key