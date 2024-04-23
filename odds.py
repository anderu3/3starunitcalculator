SHOP_SLOTS = 5

shop_odds = {
    "Level 2": {"1-cost": 1},
    "Level 3": {"1-cost": .75, "2-cost": .25},
    "Level 4": {"1-cost": .55, "2-cost": .30, "3-cost": .15},
    "Level 5": {"1-cost": .45, "2-cost": .33, "3-cost": .20, "4-cost": .02},
    "Level 6": {"1-cost": .30, "2-cost": .40, "3-cost": .25, "4-cost": .05},
    "Level 7": {"1-cost": .20, "2-cost": .33, "3-cost": .36, "4-cost": .10, "5-cost": .01},
    "Level 8": {"1-cost": .18, "2-cost": .25, "3-cost": .32, "4-cost": .22, "5-cost": .10},
    "Level 9": {"1-cost": .10, "2-cost": .20, "3-cost": .25, "4-cost": .35, "5-cost": 10},
    "Level 10": {"1-cost": .05, "2-cost": .10, "3-cost": .20, "4-cost": .40, "5-cost": .25},
}

champion_bag_pool = {
            "1-cost": 22,
            "2-cost": 20,
            "3-cost": 17,
            "4-cost": 10,
            "5-cost": 9
        }

cost1champions = ["ahri", "caitlyn", "chogath", "darius", "garen", "jax", "khazix", "kobuko", "kogmaw", "malphite", "reksai", "sivir", "yasuo"]
cost2champions = ["aatrox", "gnar", "janna", "kindred", "lux", "neeko", "qiyana", "riven", "senna", "shen", "teemo", "yorick", "zyra"]
cost3champions = ["alune", "amumum", "aphelios", "bard", "diana", "illaoi", "soraka", "tahmkench", "thresh", "tristana", "volibear", "yone", "zoe"]
cost4champions = ["annie", "ashe", "galio", "kaisa", "kayn", "leesin", "lillia", "morgana", "nautilus", "ornn", "sylas", "syndra"]
cost5champions = ["azir", "hwei", "irelia", "lissandra", "rakan", "sett", "udyr", "wukong", "xayah"]

total_number_of_3costs = len(cost3champions) * champion_bag_pool["3-cost"]
