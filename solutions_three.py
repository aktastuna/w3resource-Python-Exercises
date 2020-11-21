import numpy as np
import string

# 1. Write a Python function to find the Max of three numbers.

def get_max(x, y, z):
    lst = [x, y, z]
    return np.max(lst)

get_max(x=-5, y=3, z=10)

# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_list(lst):
    return np.sum(lst)

sum_list(lst=[1,2,3,4])

# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply_numbers(lst):
    result = 1
    for num in lst:
        result = result * num
    return result

multiply_numbers(lst=[8, 2, 3, -1, 7])

# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def rev_string(txt="tunahan"):
    return txt[:: -1]

rev_string("abcdefg")

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def get_factorial(number=5):
    result = 1
    if number == 0:
        result = 1
    elif number < 0:
        print("The number should be positive")
        result = None
    else:
        for num in range(1, number + 1):
            result = result * num
    return result

get_factorial(-1)
get_factorial(0)
get_factorial(7)

# 6. Write a Python function to check whether a number is in a given range.

def range_check(number=5, starts=1, finishes=5):
    if number in range(starts, finishes) and number != starts:
        print(number, "is in between", starts, "and", finishes)
    else:
        print(number, "is outside of", starts, "and", finishes)

range_check(number=5, starts=2, finishes=10)
range_check(number=5, starts=2, finishes=5)

# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_up_low(txt="Tunahan"):
    ups = len([s for s in txt if s in string.ascii_uppercase])
    lows = len([s for s in txt if s in string.ascii_lowercase])
    return print(" No. of Upper case characters :", ups, "\n",
                 "No. of Lower case Characters :", lows)

count_up_low(txt="The quick Brow Fox")

# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def get_unique_list(lst):
    unique_list = []
    for elem in lst:
        if elem in unique_list:
            pass
        else:
            unique_list.append(elem)
    return unique_list

get_unique_list(lst=[1,2,3,3,3,3,4,5])

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def primer_number(number):
    if number == 1:
        return False
    elif number == 2:
        return False
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True

primer_number(17)
        
# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_num(lst):
    even_list = []
    for elem in lst:
        if (elem % 2 == 0) and (elem not in even_list):
            even_list.append(elem)
        else:
            pass
    return even_list

even_num([0,0,0,1,2,3,4,5,6,7,8,8,8])

# 11. Write a Python function to check whether a number is perfect or not.
# According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
# that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). 
# Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
# Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 
# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect_number(number=6):
    if number <= 0:
        return False
    else:
        divisors = []
        for num in range(1, number):
            if number % num == 0:
                divisors.append(num)
            else:
                pass
        divisors.append(number)
        if np.sum(divisors) / 2 == number:
            return True
        else:
            return False

perfect_number(8128)

# 12. Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(txt="madam"):
    reverse_txt = txt[:: -1]
    if reverse_txt == txt:
        return True
    else:
        return False

palindrome("tunahan")

# 13. Write a Python function that prints out the first n rows of Pascal's triangle.

def pascal(threshold=5):
    triangle = [1]
    add_zero = [0]
    for row in range(max(threshold, 0)):
        triangle = [f + s for f, s in zip(triangle + add_zero, add_zero + triangle)]
        print(triangle)

pascal(threshold=10)

# 14. Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def pangrams(txt):
    letters = set(string.ascii_lowercase)
    txt = set(txt.lower())
    if letters <= txt:
        return True
    else:
        return False

pangrams("The quick brown fox jumps over the lazy dog")

# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence 
# after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

def hyphen(txt, split_char = "-"):
    elems = [char for char in txt.split(split_char)]
    elems.sort()
    print("-".join(elems))

hyphen("green-red-yellow-black-white", "-")

# 16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included). 

def number_square(threshold):
    lst = [num**2 for num in range(1, threshold + 1)]
    return print(lst)

number_square(10)
