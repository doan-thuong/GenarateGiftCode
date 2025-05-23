import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def get_fire_base():
    # Khởi tạo Firebase với file JSON credentials
    service_account_path = "E:/Download/ezg-nightfall-firebase-adminsdk-.json"
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

    # Kết nối tới Firestore
    db = firestore.client()
    doc_ref = db.collection("game_config").document("gift_code")

    return doc_ref