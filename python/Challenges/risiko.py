# In a game of RisiKo! (the Italian version of the popular board game Risk!), 
# the players throw six-sided dice to conquer territories around a World map.

# When two players contend a territory there is a battle, and they throw from 1 up to 3 dice, 
# with each die being an army sent to fight. To establish who loses armies after the battle, 
# the dice are compared starting from the highest value, and proceeding with the comparisons in 
# descending order (eliminating the dice in excess if the amount of thrown dice among the two players is different).

# When the rolls are compared, for each comparison the die of the attacking player must have a greater 
# value than the defender's die to win the fight. In the case of a tie, the defender wins the single fight. 
# The loser only loses 1 army per comparison.

# Given two arrays attacker (rolls of the attacker) and defender (rolls of the defender), implement a function 
# that returns the armies lost by the defender as an integer.

def risiko(attacker, defender):
    # Sort each array into descending order
    attacker = sorted(attacker, reverse=True)
    defender = sorted(defender, reverse=True)

    # Initiate the defender total to 0
    defender_total = 0
    
    # 
    battle = zip(attacker, defender)

    # for each attacker and defender roll in the battle
    for attacker,defender in battle:
        # if attacker roll is less than defender roll then attacker loses army
        if attacker < defender:
            continue
        # if attacker roll is equal to defender roll then attacker loses army
        elif attacker == defender:
            continue
        # if defender roll is less than attacker roll then defender loses an army
        else:
            # add lose to total armies the defender has lost
            defender_total += 1
    # return total number of armies lost to defender
    return defender_total




# risiko([3, 6, 4], [2, 5, 3])
# risiko([3, 6], [6, 4, 4])
# risiko([3, 1], [1])
# risiko([4, 4, 3], [3, 2])
# risiko([5], [3, 1, 4])
# risiko([3, 5], [3, 5])
# risiko([3, 6, 6], [6])
# risiko([5, 4], [3, 4, 3])
# risiko([3], [2, 1])
# risiko([3, 3, 3], [2, 1, 2])