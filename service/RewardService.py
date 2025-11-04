def convert_reward(type, reward_id, number, rarity, level) -> str:
    return f"{type}-{reward_id}-{number}-{rarity}-{level}"

def convert_reward_money_type(reward_id, number) ->str:
    return f"{0}-{reward_id}-{number}-{0}-{0}"

def convert_reward_item(item_id, number, rarity, level) -> str:
    return f"{1}-{item_id}-{number}-{rarity}-{level}"