import random
import numpy as np
import string
import re
from datetime import date

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

def get_numbers(start, finish):
    num_list = []
    for num in range(start, finish + 1):
        if (num % 5 == 0) and (num % 7) == 0:
            num_list.append(num)
        else:
            continue
    return print(num_list)

get_numbers(1500, 2700)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.

def temperature_converter():
    while True:
        try:
            ask_user = input("Please choose C / F: ")
        except ValueError:
            print("Error!")
            continue
        if len(ask_user) > 1:
            print("Please type C or F")
            continue
        elif ask_user not in ["c", "f", "C", "F"]:
            print("Please do not type something other than C or F")
            continue
        else:
            break

    ask_temp = int(input("Please choose " + ask_user.upper() + " degree: "))    
    if ask_user.upper() == "F":
        degree = int(round((ask_temp - 32) * 5/9))
        msg = print(ask_temp, ask_user.upper(), "degree is", degree, "in Celsius")
    else:
        degree = int(round((9 * ask_temp) / 5 + 32))
        msg = print(ask_temp, ask_user.upper(), "degree is", degree, "in Fahrenheit")
    return msg

temperature_converter()

# 3. Write a Python program to guess a number between 1 to 9

target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 100 until you get it right : '))
print('Well guessed!')

# 4. Write a Python program to construct the following pattern, using a nested for loop.

def draw_stars(max_stars=5):
    for up_side in range(max_stars):
        print("*" * up_side)

    for down_side in range(max_stars, 0, -1):
        print("*" * down_side)

draw_stars(max_stars=10)

# 5. Write a Python program that accepts a word from the user and reverse it.

def reverse_string():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        try:
            ask_user = str(input("Please type a string: "))
        except ValueError:
            print("Error!")
            continue
        if len(ask_user) <= 1:
            print("Please type a word.")
            continue
        elif [i for i in lst if str(i) in ask_user]:
            print("Please do not type any digits.")
            continue
        else:
            break

    exp_word = ask_user[::-1]
    return print(exp_word)

reverse_string()

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.

def count_even_odd(start_num = 0, finish_num = 10, increase_by = 1):
    my_range = np.arange(start_num, finish_num, 1)
    lst_odds = []
    lst_evens = []
    for num in my_range:
        if my_range[num] % 2 == 0:
            lst_evens.append(num)
        else:
            lst_odds.append(num)
    return print("Number of even numbers:", len(lst_evens),
                 "Number of odd numbers:", len(lst_odds))

count_even_odd(finish_num = 11)

# 7. Write a Python program that prints each item and its corresponding type from the following list.

lst = []
while len(lst) < 10:
    ask_user = input("Please give a value: ")
    lst.append(ask_user)

for i in lst:
    print(i, "değişkeninin data tipi", type(i), "dir.")

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. Note : Use 'continue' statement. Expected Output : 0 1 2 4 5

def except_3_6():
    for i in range(7):
        if (i == 3 or i == 6):
            continue
        print(i, end = " ")

except_3_6()

# 9) Write a Python program to get the Fibonacci series between 0 to 50

def fib_nums(threshold = 10):
    fib_list = []
    for num in range(threshold):
        if num == 0:
            fib_list.append(num)
        elif num == 1:
            fib_list.append(num)
        else:
            fib_list.append(fib_list[num - 1] + fib_list[num - 2])
    return print(fib_list)

def input_value():
    while True:
        try:
            number = int(input("Please give amount of numbers you want to see: "))
            print("Done!")
        except ValueError:
            print("Please do not write any characters.")
            continue
        if number <= 0:
            print("Please give the number greater than zero.")
            continue
        else:
            break
    return number

number = input_value()
fib_nums(threshold = number)

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

def fizzbuzz(my_range):
    for num in range(my_range):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
            continue
        elif num % 5 == 0:
            print("buzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        else:
            print(num)
            continue

fizzbuzz(51)

# 11. Write a Python program which takes two digits m (row) and n (column) as input and generates a 
# two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

def matrix_creator():
    while True:
        try:
            x = int(input("How many rows do you want? "))
            y = int(input("How many columns do you want: "))
            print("The matrix is {0} x {1}".format(x, y))
        except ValueError:
            print("Please do not type anything other than integer.")
            continue
        if x < 0 or y < 0:
            print("Matrix dimensions can not be less than 0")
            continue
        else:
            break
        
    x_nums = np.arange(x)
    y_nums = np.arange(y)
    matrix_ = np.zeros((x, y))
    for row in x_nums:
        for col in y_nums:
            matrix_[row, col] = row * col
    return matrix_

matrix_creator()

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and 
# prints the lines as output (all characters in lower case).

# I DID NOT UNDERSTAND THIS PROBLEM.

# 13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its 
# input and print the numbers that are divisible by 5 in a comma separated sequence. Go to the editor
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010

def comma_separator():
    while True:
        try:
            user_input = float(input("Please type a number: "))
        except ValueError:
            print("Please do not type something other than number.")
            continue
        else:
            break
    user_input = format(user_input, ".4f").split(".")[1]
    if (user_input[0] == "0") and (user_input[1] == "0") and (user_input[2] == "0"):
        print("After comma, all the digits are 0. Try again.")
        pass
    elif (user_input[0] == "0") and (user_input[1] == "0"):
        print("After comma, first two digits are 0. Try again.")
        pass
    elif user_input[0] == "0":
        print("After comma, first digit is zero. Try again.")
        pass
    else:
        if int(user_input) % 5 != 0:
            print("Cannot be divided by 5.")
            pass
        else:
            print(user_input)
        pass

comma_separator()

# 14. Write a Python program that accepts a string and calculate the number of digits and letters.

def char_counter(user_input):
    str_num = lst_num = 0
    letters_ = string.ascii_letters
    numbers_ = [str(i) for i in range(10)]
    for char in user_input:
        if char in letters_:
            str_num += 1
        elif char in numbers_:
            lst_num += 1
        else:
            continue
    return print("Letters", str_num,
                 "Digits", lst_num, sep="\n")

char_counter("Tunahan12345")

# 15. Write a Python program to check the validity of password input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

def create_password():
    while True:
        try:
            ask_user = input("Please type your password: ")
        except ValueError:
            print("System is interrupted.")
            continue
        if len(ask_user) < 6:
            print("Your password must be more than 6 characters.")
            continue
        elif len(ask_user) > 16:
            print("Your password must be less than 16 characters.")
            continue
        elif not re.search("[a-z]", ask_user):
            print("Your password must contain at least 1 lower case letter.")
        elif not re.search("[A-Z]", ask_user):
            print("Your password must contain at least 1 upper case letter.")
            continue
        elif not re.search("[0-9]", ask_user):
            print("Your password must contain at least 1 digit.")
            continue
        elif not re.search("[$#@.]", ask_user):
            print("Your password must contain at least 1 special character.")
            continue
        else:
            break
    while True:
        try:
            ask_password_again = input("Please type your password again: ")
        except ValueError:
            print("System is interrupted.")
        if ask_password_again == ask_user:
            print("The password has set.")
            break
        else:
            print("The passwords are not matched. Please try again.")
            continue

create_password()

# 16. Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.

def even_detector(start, finish):
    lst_odds = [str(num) for num in np.arange(1, 10, 2)]
    for digit in range(start, finish + 1):
        if set(str(digit)).issubset(lst_odds):
            print(digit)
        else:
            continue

even_detector(start=100, finish=400)

# 31. Write a Python program to calculate a dog's age in dog's years. Go to the editor
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

def dog_age():
    while True:
        try:
            input_user = int(input("Input a dog's age in human years: "))
        except ValueError:
            print("Please do not type something other than numbers.")
            continue
        if input_user < 0:
            print("Age can't be less than 0.")
            continue
        else:
            break
    age = None
    if input_user <= 2:
        age = input_user * 10.5
        print("The dog's age in dog's years is", age)
    else:
        age = 10.5 * 2 + (input_user - 2) * 4
        print("The dog's age in dog's years is", int(age))

dog_age()

# 32. Write a Python program to check whether an alphabet is a vowel or consonant.

def vowels_consonent():
    vowels = "aeiou"
    while True:
        try:
            user_input = input("Input a letter of the alphabet: ").lower()
        except ValueError:
            print("Please do not type any numbers or special characters.")
            continue
        if len(user_input) > 1:
            print("Please type only a letter.")
            continue
        elif user_input in [str(num) for num in np.arange(0, 10, 1)]:
            print("Please do not type digits.")
            continue
        elif not re.search("[a-z]", user_input):
            print("Please do not type special characters.")
            continue
        else:
            break
    
    if user_input in vowels:
        print(user_input, "is a vowel.")
    else:
        print(user_input, "is a consonant.")

vowels_consonent()

# 33. Write a Python program to convert month name to a number of days.

def month_day():
    lst_months = [date(1900, month , 1).strftime('%B') for month in np.arange(1, 13, 1)]
    map_month = map(str.lower, (lst_months))
    lst_month = list(map_month)
    while True:
        try:
            user_input = input("List of months: January, February, March, April, May, June, July, \n August, September, October, November, December \n Input the name of Month: ")
        except ValueError:
            print("System is interrupted.")
            continue
        if user_input.lower() not in lst_month:
            print("Pleae do not type something other than months.")
            continue
        else:
            break
    if user_input.lower() in ["january", "march", "may", "july", "august", "october", "december"]:
        print("No. of days: 31 days.")
    elif user_input.lower() == "february":
        print("No. of days: 28/29 days.")
    else:
        print("No. of days: 30 days.")

month_day()

# 34.  Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum_two_digits(x=0, y=0):
    sum_ = None
    if (x + y >= 15) and (x + y <= 20):
        sum_ = 20
    else:
        sum_ = x + y
    return sum_

sum_two_digits(-1,16)

# 35. Write a Python program to check a string represent an integer or not.

def integer_or_not():
    user_input = input("Please type something: ").lower()
    if not re.search("[0-9]", user_input):
        print("It is not an integer.")
    elif re.search("[0-9]", user_input) and re.search("[a-z]", user_input):
        print("It is not an integer")
    else:
        print("It is an integer.")

integer_or_not()

# 36. Write a Python program to check a triangle is equilateral, isosceles or scalene. Go to the editor
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

def triangle_type():
    while True:
        try:
            print("Input lengths of the triangle sides: ")
            x = int(input("x: "))
            y = int(input("y: "))
            z = int(input("z: "))
        except ValueError:
            print("Triangle sides can not be characters.")
            continue
        if x <= 0 or y <= 0 or z <= 0:
            print("Sides can not be less than or eqaul to 0.")
            continue
        else:
            break
    lst = [x, y, z]
    if lst.count(x) == 3:
        print("Equilateral Triangle")
    elif lst.count(x) == 2:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

triangle_type()

# 40. Write a Python program to find the median of three values.

def find_median():
    number_list = []
    while True:
        try:
            user_input = input("If you want to stop adding numbers, type 'exit()'. Please type a number: ")
        except ValueError:
            print("Please  do not type any strings.")
            continue
        if re.search("[a-z]", user_input.lower()) and ("(" not in user_input or ")" not in user_input):
            print("Please do not type characters.")
            continue
        elif user_input == "exit()":
            break
        else:
            number_list.append(int(user_input))
            continue            
    return np.median(number_list)

find_median()

# 42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

def sum_average():
    num_list = []
    while True:
        try:
            user_input = int(input("Input the numbers: "))
        except ValueError:
            print("Please do not type strings.")
            continue
        if user_input != 0:
            num_list.append(user_input)
            continue
        else:
            break
    return print("The sum of the numbers: ", np.sum(num_list),"\n",
                 "The average of the numbers: ", np.mean(num_list))

sum_average()

# 43. Write a Python program to create the multiplication table (from 1 to 10) of a number.

def multiplication_table():
    while True:
        try:
            user_input = int(input("Input a number: "))
        except ValueError:
            print("Please do not type strings.")
            continue
        if user_input < 0:
            print("Please do not type numbers less than 0.")
            continue
        else:
            for i in np.arange(1, 11, 1):
                print(user_input, "x", i, "=", user_input * i)
            break

multiplication_table()

# 44. Write a Python program to construct the following pattern, using a nested loop number.

def number_triange():
    for num in range(10):
        print(str(num) * num)

number_triange()
