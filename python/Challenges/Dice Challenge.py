# Dice Roll
# In role-playing games, the standard notation for dice rolls is nds, where n is the number of die to roll and s is how many sides each die has. 
# For example 2d6 means roll two six-sided dice, 1d12 means roll one 12-sided die. 

# Write a function to simulate a role-playing game dice roll. The function should accept a parameter which must conform to the standard notation. 
# Return None if the format is invalid. The function should generate a random roll for each die and return a list containing the results.

# Example:
# roll('2d6')     # [5, 2]
# roll('3d10')    # [1, 9, 7]

# Extra
# Modify the function so that, in addition to the list of rolls, it also returns the sum of the rolled dice and the highest roll.

# Example:
# roll('2d6')    # if result was [6, 3], returns [6,3] and 9 (sum) and 6 (highest)


import random

def dice_roll(nds):

    # Split the input of dice_roll into a list separating when 'd' is found
    nds = nds.split('d')

    # If the input is not in the correct notation return none
    if nds[0].isnumeric() == False or nds[1].isnumeric() == False:
        return None

    # The first element of the list is equal to the number of die
    dice_number = int(nds[0])
    # The second element of the list is equal to the number of sides on the dice
    dice_sides = int(nds[1])
    # Define total as 0 and create an empty list of results
    total = 0
    result=[] 
    # A roll occurs for each number of dice
    for roll in range(dice_number):
        # The result of the roll is a random number between 1 and how many sides of the dice
        roll = random.randint(1,dice_sides)
        # The result of the roll is added to the list of results
        result.append(roll)
        # The result of the roll is added into the total 
        total += roll

    # Equals the highest number in the results list
    highest_value  = max(result)

    print(f"You have rolled {result}.")
    print(f"The sum of these values is [{total}] and the highest roll was [{highest_value}]")



