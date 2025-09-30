# FILE NAME - coin_toss.py

# NAME: Michael Glazier
# DATE: 09/30/2025
# BRIEF DESCRIPTION: return coin toss based off a random number

########## ENTER YER CODE BELOW THIS LINE ##########

import random

def main():
    
    coin_toss = random.randint(1,101) 
    
    if coin_toss >= 51:
        coin_result = "Tails"
    else:
        coin_result = "Heads"

    print("===== Coin Flipper =====")
    print(coin_result)

main()

########### END YER CODE ABOVE THIS LINE ###########

########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 

ensuring entire range was included





'''
