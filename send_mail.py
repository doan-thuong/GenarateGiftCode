from datetime import datetime, timezone

import service.SupabaseService as spbS

table_name = "mail_box"
title = "Compensation Reward"
des = "Hello Player,\nPlease accept this reward as compensation for any inconvenience you’ve experienced. Enjoy!\n— Game Support Team"
# des = "Hello Player,\nWe’re sorry for the issue that caused you to miss your reward. Please accept this compensation as an apology\nThank you for your understanding!\n— Game Support Team"
create_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
mail_status = 0
mail_reward_status = 0
reward_code = "0-1-400-0-0"
uid = "dL4CiENResc2BqlrQfuZe5qfGRI3"
mail_id = f"compensation_reward_{datetime.now(timezone.utc).date()}_user_id_{uid}"
reward_bonus = 0

res = spbS.insert_mail(mail_id, create_at, title, des,mail_status,
                mail_reward_status, reward_code, uid,reward_bonus,
                table_name)

if res:
    print("insert success")