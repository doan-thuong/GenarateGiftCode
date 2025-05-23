

def handle_packs(packs_old):
    packs_new = []

    if packs_old:
        for pack in packs_old:
            packs_new.append({
                "packId": int(pack[0]),
                "packType": int(pack[1])
            })
    
    return packs_new

def handle_reward(reward_old):
    reward_new = []

    if reward_old:
        for reward in reward_old:
            reward_new.append({
                "resId": int(reward[0]),
                "resLevel": int(reward[1]),
                "resNumber": int(reward[2]),
                "resRarity": int(reward[3]),
                "resType": int(reward[4])
            })

    return reward_new

def handle_pack_in_gift_code(packs_from_user):
    pack_split_dash = []
        
    if packs_from_user:
        pack_split_enter = list(map(str, packs_from_user.split("\n")))

        for pack in pack_split_enter:
            pack_split_dash.append(pack.split("-"))

    return pack_split_dash

def handle_reward_in_gift_code(rewards_from_user):
    reward_split_dash = []

    if rewards_from_user:
        reward_split_enter = list(map(str, rewards_from_user.split("\n")))

        for reward in reward_split_enter:
            reward_split_dash.append(reward.split("-"))

    return reward_split_dash