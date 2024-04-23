import random

SHOP_SLOTS = 5

game = Gamestate(current_comp="", champ_gone=[], other_champs=[], level=0,percent_of_hitting=0)

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
