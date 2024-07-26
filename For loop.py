#Print First 10 natural numbers using while loop
#for n in range(1,11):
#   print(n)

# Print First 10 natural numbers using while loop
print("Pattern Numbers")
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end ='')
        print(" ")