import random

SHOP_SLOTS = 5

class Gamestate:

    def __init__(self, current_comp, champ_gone, other_champs, level, percent_of_hitting):
        self.current_comp = ""
        self.champ_gone = []
        self.other_champs = []
        self.level = 0
        self.percent_of_hitting = 0
        self.champion_bag_pool = {
            "1-cost": 22,
            "2-cost": 20,
            "3-cost": 17,
            "4-cost": 10,
            "5-cost": 9
        }

game = Gamestate(current_comp="", champ_gone=[], other_champs=[], level=0,percent_of_hitting=0)
cost1champions = ["ahri", "caitlyn", "chogath", "darius", "garen", "jax", "khazix", "kobuko", "kogmaw", "malphite", "reksai", "sivir", "yasuo"]
cost2champions = ["aatrox", "gnar", "janna", "kindred", "lux", "neeko", "qiyana", "riven", "senna", "shen", "teemo", "yorick", "zyra"]
cost3champions = ["alune", "amumum", "aphelios", "bard", "diana", "illaoi", "soraka", "tahmkench", "thresh", "tristana", "volibear", "yone", "zoe"]
cost4champions = ["annie", "ashe", "galio", "kaisa", "kayn", "leesin", "lillia", "morgana", "nautilus", "ornn", "sylas", "syndra"]
cost5champions = ["azir", "hwei", "irelia", "lissandra", "rakan", "sett", "udyr", "wukong", "xayah"]

total_number_of_3costs = len(cost3champions) * game.champion_bag_pool["3-cost"]

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


#Input how much of that specific 3 cost you have
currently_owned_unit = int(input("How many copies of this unit do you have?: "))

#Input how much of that specific 3 cost others have
others_owned_unit = int(input("How many copies do other players have of this unit?: "))

#Input how much 3 costs are out there thats not that unit
other_units_that_cost = int(input("How many 3 star copies are taken?: "))
#Input your level

user_level = int(input("What is your level?: "))
#Input gold (extra functionality)
#Return percent of hitting 3 star at your level

def chance_to_roll():

#Return percent of hitting at that gold (extra)


one_roll = shop_odds["Level 7"]["3-cost"] ** SHOP_SLOTS
print(one_roll)

# Each shop has
