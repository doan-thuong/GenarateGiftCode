from datetime import datetime, timezone

import service.SupabaseService as spbS

table_name = "mail_box"
title = "Server Booster Rewards!"
des = "Greetings, Kings!\nThank you for supporting the Nightfall Discord server. Here’s a small gift from us—wishing you victorious battles ahead!"
create_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
mail_status = 0
mail_reward_status = 0
reward_code = "0-719-50000-0-0,0-721-20-0-0"
uids = [
    "moMpDfFDUbTQivVVPdefXMqUARg2",
    "q3PgSFzDqTPbtvT3LvsD3XyOjSS2",
    "Ie6ICX2mQSXSSffglT00udHiwHl1",
    "z31TQ8lG2Sfk8B1rwiTFhK6riIw2",
    "ESsnnzUjlwU32UxCcB5kFasYiuh1"
]
# uids =[
#     "cYrVVa6KjBdc64yaoxoi6uC1zkA3",
#     "9rv5JR1NkZRdRU0GpyXnSkN9wgv2"
# ]
reward_bonus = 0

for uid in uids:
    mail_id = f"compensation_reward_{datetime.now(timezone.utc).date()}_user_id_{uid}"
    res = spbS.insert_mail(mail_id, create_at, title, des,mail_status,
                mail_reward_status, reward_code, uid,reward_bonus,
                table_name)

    if res:
        print("insert success")