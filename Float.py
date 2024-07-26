two_digit_number = input()

# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

(type(two_digit_number))  # Check the data type of two_digit_number

# Extract the digits directly from the string input
first_digit_number = int(two_digit_number[0])
second_digit_number = int(two_digit_number[1])

# Sum the digits
sum_of_digits = first_digit_number + second_digit_number

# Print the result
print(f"{first_digit_number} + {second_digit_number} = {sum_of_digits}")
