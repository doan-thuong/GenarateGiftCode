def mail_box(mail_id, create_at, title, des, status, reward_status, reward, player_id):
    return {
        "mail_id": mail_id,
        "create_at": create_at,
        "localize_title": title,
        "localize_des": des,
        "mail_status": status,
        "mail_reward_status": reward_status,
        "rewards_code": reward,
        "player_id": player_id
    }