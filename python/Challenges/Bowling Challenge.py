# Write a function to calculate the score for one "frame" of ten-pin bowling. 
# An entire game consists of 10 frames, with up to 2 balls bowled per frame.

# Due to how the scoring works, you will need to know how many pins were knocked down by the last 
# 3 balls bowled in order to calculate the total score for the frame.

# The scoring rules are:
# 1 point for each pin knocked down (so between 0 and 10)
# If it's a strike (all 10 pins knocked down with 1 ball), add the total of the next 2 balls
# If it's a spare (all 10 pins knocked down with 2 balls), add the next ball

def calc_frame(x, y, z):
    # Scoring neither a spare or a strike 
    if (x+y)<10:
        result = x + y
    # If a spare or strike were bowled
    else:
        result = x + y + z

    return result