names=["anglena","melon","helena","grace","will"]
import random
num_items = len(names)
random = random.randint(0, num_items - 1)
print(f"{names[random]} is going to buy the meal today!")