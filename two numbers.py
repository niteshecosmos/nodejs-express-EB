two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
type(two_digit_number)
first_digit_number = int(two_digit_number[0])
second_digit_number = int(two_digit_number[1])
sum_of_digits = first_digit_number + second_digit_number
print(f"{sum_of_digits}")