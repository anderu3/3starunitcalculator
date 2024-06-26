import random

def shop_prob_3cost():
    return random.randint(1, 100)

def draw_champion(champions_pool):
    return random.choice(champions_pool)

def initialize_3cost_pool():
    champions_pool = ["alune", "amumu", "aphelios", "bard", "diana", "illaoi", "soraka", "tahmkench", "thresh", "tristana", "volibear", "yone", "zoe"]
    champion_bag_pool = {champion: 17 for champion in champions_pool}
    total_champions = len(champions_pool) * 17
    return champions_pool, champion_bag_pool, total_champions

def check_spelling(target):
    if target == "tahm" or target == "kench":
        return "tahmkench"
    elif target == "voli":
        return "volibear"
    elif target == "raka":
        return "soraka"
    elif target == "trist":
        return "tristana"
    else:
        return target

def start_reroll(target, taken_champs, taken_3costs):
    champions_pool, champion_bag_pool, total_champions = initialize_3cost_pool()
    reroll = 0
    bought_champions = {champion: 0 for champion in champions_pool}
    champion_bag_pool[target]  = champion_bag_pool[target] - taken_champs
    total_champions = total_champions - taken_3costs
    while bought_champions[target] < 9:
        reroll += 1
        # Simulate 5 champ cards per reroll
        shops = [[] for i in range(5)] 
        for i in range(len(shops)): 
            # Check to see if it hit 36%
            roll = shop_prob_3cost()
            if 1 <= roll <= 36: 
                # If 36% passed, grab random 3-cost that is still in the pool
                champion = draw_champion(champions_pool)
                # If no more of that champ, reroll champ
                if champion_bag_pool == 0:
                    champion = draw_champion(champions_pool)
                if champion_bag_pool[champion] > 0: 
                    # Add to shop
                    shops[i].append(champion)
                    # How many I have
                    bought_champions[champion] += 1
                    # Reduce one from total pool and pool of specific champ
                    champion_bag_pool[champion] -= 1
                    total_champions -= 1
        # Check if the desired champion has been collected 9 times
        if bought_champions[target] == 9:
            break

    return reroll, bought_champions, total_champions

target = input("Enter the 3-cost champion you want to 3-star: ").lower()
target = check_spelling(target)
taken_champs = int(input("How many of these champs are taken?: "))
taken_3costs = int(input("How many of 3-costs are out of the pool?: "))
total_gold = 0
sim_count = 10000
original_sim_count = sim_count

while sim_count > 0:
    reroll, bought_champions, total_champions = start_reroll(target, taken_champs, taken_3costs)
    total_gold += reroll
    sim_count -= 1



print(f"From a sim of {original_sim_count}, it would cost you on average {int((total_gold * 2) / original_sim_count)} gold to hit a 3-star {target}")
# print("Total 3-cost champions shown in shops:")
# for champion, count in bought_champions.items():
#     print(f"{champion} - {count}")
