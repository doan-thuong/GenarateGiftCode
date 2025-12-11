def mail_box(mail_id, create_at, title, des, status, reward_status, reward, player_id, bonus_percent):
    return {
        "mail_id": mail_id,
        "created_at": create_at,
        "localize_title": title,
        "localize_des": des,
        "mail_status": status,
        "mail_reward_status": reward_status,
        "rewards_code": reward,
        "player_id": player_id,
        "reward_bonus_percent": bonus_percent
    }

def whitelist_device(device_id, name, device_type):
    return {
        "device_id": device_id,
        "name": name,
        "device_type": device_type
    }