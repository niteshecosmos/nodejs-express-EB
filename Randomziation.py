#Generate 3 random number int between 100 and 999 divisible by 5

#import random

#random_number = random.randint(100, 999)
#user_number= int(input("Enter your Number:"))
#if user_number % 5 == 0:
 #   print("This value divisble by 5")
#else:
 #   print("This value not divisble by 5")
 
# Random lottery ticket pick generate the 100 random lottery tickets in the and pick two lottery ticket from its a winner
#import random 


import random
random_number = random.randint(1, 100)

Person = int(input("Enter your lottery number (between 1 and 100): "))

if Person == random_number:
    print("Congratulations! You've won!")
else:
    print("Sorry, you are not the winner. The winning number was:", random_number)


# Generate 6 digit random secure OTP

import random
random_number = random.randint()
 