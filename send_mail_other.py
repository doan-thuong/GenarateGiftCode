from config import Enum
from service import RewardService as reward
import service.SupabaseService as spbS

from datetime import datetime, timezone

create_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
date_now = datetime.now(timezone.utc).date()

table_name = Enum.TableName.MAIL_BOX
title = Enum.MailComponent.TITLE_COMPENSATION_REWARD
des = Enum.MailComponent.DES_COMPENSATION_REWARD

mail_status = Enum.StatusMail.CanOpen.value
mail_reward_status = Enum.StatusRewardMail.CanClaim.value

uid = "zphqTwqyeOcW2UQRxb9GROEnuP62"
mail_id = f"compensation_reward_{date_now}_uid_{uid}"

reward_code = reward.convert_reward_money_type(Enum.MoneyType.DailyChallengeCoin, 2000)
reward_bonus = 0

res = spbS.insert_mail(mail_id, create_at, title, des, mail_status,
                       mail_reward_status, reward_code, uid, reward_bonus,
                       table_name)

if res:
    print("insert success")