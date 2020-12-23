import sys
from datetime import datetime
import math
import calendar
import os
import platform
import site
from subprocess import call
import multiprocessing
import time
import glob
import random
from functools import reduce
import json

# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

print("Twinkle, twinkle, little star, \n\t How I wonder what you are! \n\t\t Up abover the world so high, \n\t\t Like a diamond in the sky \nTwinkle, twinkle, little star, \n\t How I wonder what you are")

# 2. Write a Python program to get the Python version you are using.

print(sys.version)

# 3. Write a Python program to display the current date and time.

print((datetime.today().strftime("%Y-%m-%d %H:%M:%S")))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.

radius_ = float(input("Your radius is: "))
print("Are =", math.pi * radius_**2)

# 5. Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.

user_inp = input("Please type your name and surname with space between: ")
print(user_inp.split()[1], user_inp.split()[0])

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user 
# and generate a list and a tuple with those numbers.

chars = input("Plesae type some numbers and put comma between them: ")
print(list(chars.split(",")))
print(tuple(chars.split(",")))

# 7. Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

print(input("Please type your file with extension: ").split(".")[1])

# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

print("The examination will start from : %d / %d / %d"%(11, 12, 2014))

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

number = input("Please type a number: ")
print(int(number) + int(number + number) + int(number + number + number))

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# Click me to see the sample solution

print(abs.__doc__)

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

print(calendar.month(2011, 6))

# 13. Write a Python program to print the following here document. Go to the editor
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

tuple_one = (2014, 7, 2)
tuple_two = (2035, 11, 28)
day_one = datetime.strptime("%i-%i-%i"%tuple_one, "%Y-%m-%d")
day_two = datetime.strptime("%i-%i-%i"%tuple_two, "%Y-%m-%d")

print((day_two - day_one).days)

# 15. Write a Python program to get the volume of a sphere with radius 6

radius_ = float(input("Please type the radius: "))
print("The volume of the sphere is:", 4/3 * (math.pi * radius_**3))

# 16. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

user_inp = int(input("Please type a number: "))
print(abs(user_inp - 17)) if user_inp <= 17 else print((user_inp - 17) * 2)

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

user_inp = int(input("Please type a number: "))
print(True if abs(user_inp - 1000) <= 100 or abs(user_inp - 2000) <= 100 else False)

# 18. Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

num_one = int(input("Please type number: "))
num_two = int(input("Please type number: "))
num_three = int(input("Please type number: "))
num_list = [num_one, num_two, num_three]

print(sum(num_list) * 3 if num_list.count(num_list[0]) == 3 else sum(num_list))

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged.

chars = input("Please type a sentence: ")
print(chars if chars[0:2].capitalize() == "Is" else "Is" + chars)

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

inp_str = input("Please type a word: ")
inp_int = int(input("Please type an integer: "))

print(inp_str * inp_int)

# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
# print out an appropriate message to the user.

inp_int = (int(input("Please type a number: ")))
print("The number is even." if inp_int%2 == 0 else ("The number is negative." if inp_int < 0 else "The number is odd."))

# 22. Write a Python program to count the number 4 in a given list.

lst = []
stopper = True
while stopper:
    user_inp = input('Please type number. If you want to stop adding numbers, please type "stop": ')
    if user_inp.lower() == 'stop':
        stopper = False
        break
    else:
        lst.append(int(user_inp))
        continue

print(lst.count(4))

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2.

inp_str = input("Please type something: ")
inp_int = int(input("Number of copies: "))
print(inp_str * inp_int if len(inp_str) < 2 else inp_str[0:2] * inp_int)

# 24. Write a Python program to test whether a passed letter is a vowel or not.

inp_str = input("Please type a letter: ")
print("Vowel" if inp_str in "aeiou" else ("It is not a letter.") if len(inp_str) > 1 else "Not vowel")

# 25. Write a Python program to check whether a specified value is contained in a group of values.

lst = []
stopper = True
while stopper:
    user_inp = input('Please type number. If you want to stop adding numbers, please type "stop": ')
    if user_inp.lower() == 'stop':
        stopper = False
        break
    else:
        lst.append(int(user_inp))
        continue

num = int(input("Please type a number: "))
print(True if num in lst else False)

# 26. Write a Python program to create a histogram from a given list of integers.

lst = []
stopper = True
while stopper:
    user_inp = input('Please type number. If you want to stop adding numbers, please type "stop": ')
    if user_inp.lower() == 'stop':
        stopper = False
        break
    else:
        lst.append(int(user_inp))
        continue

for num in lst:
    print("*" * num)

# 27. Write a Python program to concatenate all elements in a list into a string and return it.

lst = []
stopper = True
while stopper:
    user_inp = input('Please type number. If you want to stop adding numbers, please type "stop": ')
    if user_inp.lower() == 'stop':
        stopper = False
        break
    else:
        lst.append(int(user_inp))
        continue

disp_ = ""
for chars in lst:
    disp_ += str(chars)
print(disp_)

# 28. Write a Python program to print all even numbers from a given numbers list in the same order 
# and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
           399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
           958,743, 527]

disp_list = []
num = 0
threshold = 237
while numbers[num] != threshold:
    if numbers[num] % 2 == 0:
        disp_list.append(numbers[num])
        num += 1
        continue
    else:
        num += 1
        continue
disp_list.append(threshold)
print(disp_list)

# 29. Write a Python program to print out a set containing all the colors from color_list_1 
# which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

color_list_1.difference(color_list_2)

# 30. Write a Python program that will accept the base and height of a triangle and compute the area.

base = int(input("Please type the length of base: "))
height = int(input("Please type the height of base: "))

print("The area is: " + str(base*height*1/2) if base > 0 and height > 0 else "Base or Height is less than or equal to 0 so the area cannot be calculated.")

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

num_one = int(input("Please type a number: "))
num_two = int(input("Please type a number: "))
lst = [num_one, num_two]
max_num = []

for num in range(2, max(lst)):
    if (num_one % num == 0) and (num_two % num == 0):
        max_num.append(num)
        continue
    else:
        pass
print(max(max_num))

# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.



# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num_one = int(input("Please type a number: "))
num_two = int(input("Please type a number: "))
num_three = int(input("Please type a number: "))
lst = [num_one, num_two, num_three]

print(0 if (lst.count(lst[0]) == 2) or (lst.count(lst[1]) == 2) or (lst.count(lst[2]) == 2) else sum(lst))

# 34. Write a Python program to sum of two given integers. However, 
# if the sum is between 15 to 20 it will return 20.

num_one = int(input("Please type a number: "))
num_two = int(input("Please type a number: "))
lst = [num_one, num_two]
print(20 if sum(lst) >= 15 and sum(lst) <= 20 else num_one + num_two)

# 35. Write a Python program that will return true 
# if the two given integer values are equal or their sum or difference is 5.

num_one = int(input("Please type a number: "))
num_two = int(input("Please type a number: "))

print(True if (num_one == num_two) or (num_one + num_two) == 5 or abs(num_one - num_two) == 5 else False)

# 36. Write a Python program to add two objects if both objects are an integer type.

def adding_two_nums(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Inputs are not integer.")
    return x + y

adding_two_nums(5, "test")

# 37. Write a Python program to display your details like name, age, address in three different lines.

def printer(name, age, address):
    print("name: {} \nage: {} \naddress: {}".format(name, age, address))

printer("Tunahan", 50, "Turkey")

# 38. Write a Python program to solve (x + y) * (x + y). Go to the editor
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

def func(x, y):
    return ((x + y) ** 2)

func(5, 6)

# 39. Write a Python program to compute the future value of a specified principal 
# amount, rate of interest, and a number of years. Go to the editor
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def calculation_(amt, interest, years):
    return (amt * (1 + 0.01 * interest) ** years)

calculation_(10000, 3.5, 7)

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

# Solution 1:

def distance_calculator(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1/2)

# Solution 2:

def distance_calculator2(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

distance_calculator([4, 0], [6, 6])
distance_calculator2([4, 0], [6, 6])

# 41. Write a Python program to check whether a file exists.

os.path.isfile(r"..../solutions_four.py")

# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.



# 43. Write a Python program to get OS name, platform and release information.

print(os.name)
print(platform.system())
print(platform.release())

# 44. Write a Python program to locate Python site-packages.

print(site.getsitepackages())

# 45. Write a python program to call an external command in Python.

call(["ls", "-l"])

# 46. Write a python program to get the path and name of the file that is currently executing.

print("Current File Name : ",os.path.realpath(__file__))

# 47. Write a Python program to find out the number of CPUs using.

multiprocessing.cpu_count()

# 48. Write a Python program to parse a string to Float or Integer.

def parse_str_to_int(char, type_):
    if type_ == "float":
        char = float(char)
    else:
        char = int(float(char))
    return char

parse_str_to_int("2.34532", "int")

# 49. Write a Python program to list all files in a directory in Python.

os.listdir(r"C:\Users\Ezgi\Desktop")

# 50. Write a Python program to print without newline or space.

for num in range(10):
    print("-", end="")

# 51. Write a Python program to determine profiling of Python programs.
# 52. Write a Python program to print to stderr.
# 53. Write a python program to access environment variables.
# 54. Write a Python program to get the current username
# 55. Write a Python to find local IP addresses using Python's stdlib
# 56. Write a Python program to get height and width of the console window.

# 57. Write a program to get execution time for a Python method.

start_ = datetime.now()
counter = 0
while counter > 100:
    counter += 1
finish_ = datetime.now()
duration_ = finish_ - start_
print("It took {} seconds\n{} microseconds to finish the code".format(duration_.seconds,
                                                                      duration_.microseconds))
# 58. Write a python program to find the sum of the first n positive integers.

def sum_numbers(lst):
    positive_numbers = []
    for num in lst:
        if num > 0:
            positive_numbers.append(num)
            return positive_numbers
        else:
            pass

sum_numbers([-1, -5, 2, 3])

# 59. Write a Python program to convert height (in feet and inches) to centimeters.

def height_converter(height_):
    print("Height in feet is: {}\nHeight in inches {}".format(height_*0.0328084, height_*0.393700787))

height_converter(180)

# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.

def hypotenuse_calculator(x, y):
    if not (isinstance(x, int) or isinstance(y, int) or x > 0 or y > 0):
        raise TypeError("Side cannot be less than or equal to zero or a string.")
    else:
        hypotenuse = math.sqrt(x**2 + y**2)
    return hypotenuse

hypotenuse_calculator(3, 4)

# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def feet_converter(feet_):
    if not (isinstance(feet_, int) or isinstance(feet_, float)):
        raise TypeError("Feet cannot be something other than number.")
    else:
        inches = feet_ * 12
        yards = feet_ * 0.333333333
        miles = feet_ * 0.000189393939
    print(feet_, "feet is {} inches,\n{} yards, and\n{} miles".format(inches, yards, miles))

feet_converter(100)

# 62. Write a Python program to convert all units of time into seconds.

def time_converter():
    days_ = int(input("Days: "))*24*60*60
    hours_ = int(input("Hours: "))*60*60
    minutes_ = int(input("Minutes: "))*60
    seconds_ = int(input("Seconds: "))
    return ("The amount of seconds is:", days_ + hours_ + minutes_ + seconds_)

time_converter()

# 63. Write a Python program to get an absolute file path.

os.path.abspath("solutions_four.py")

# 64. Write a Python program to get file creation and modification date/times.

time.ctime(os.path.getctime(os.path.abspath("solutions_four.py")))
time.ctime(os.path.getmtime(os.path.abspath("solutions_four.py")))

# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

def time_convert(seconds_):
    day_ = seconds_*1/(24*60*60)
    hour_ = seconds_*1/(60*60)
    minute_ = seconds_*1/(60)
    print("%i day(s) %i hour(s) %i minute(s) %i second(s) "%(day_, hour_, minute_, seconds_))

time_convert(172800)

# 66. Write a Python program to calculate body mass index.

def body_mass(weight, height):
    return round((weight / height**2), 2)

body_mass(85, 5.8)

# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, 
# a millimeter of mercury (mmHg) and atmosphere pressure.

def converter(kilopascals):
    pounds = kilopascals * 0.145
    mercury = kilopascals * 7.50061683
    atmospheres = kilopascals * 0.00986923267
    print(kilopascals, "is %e pounds, %e mercury and %e atmospheres"%(pounds, mercury, atmospheres))

converter(100)

# 68. Write a Python program to calculate the sum of the digits in an integer.

def num_sum(number):
    final_sum = 0
    for num in str(number):
        final_sum += float(int(num))
    return final_sum

num_sum(int(input("Please type a number: ")))

# 69. Write a Python program to sort three integers without using conditional statements and loops.

int1 = int(input("Plesae type a number: "))
int2 = int(input("Plesae type a number: "))
int3 = int(input("Plesae type a number: "))

minimum = min(int1, int2, int3)
maximum = max(int1, int2, int3)
middle = (int1 + int2 + int3) - minimum - maximum

print(minimum, middle, maximum)

# 70. Write a Python program to sort files by date.

files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# 71. Write a Python program to get a directory listing, sorted by creation date.
# 72. Write a Python program to get the details of math module.

math.__doc__
dir(math)

# 73. Write a Python program to calculate midpoints of a line.

p1 = [2, 2]
p2 = [4, 4]

middle_point = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
print(middle_point)

# 74. Write a Python program to hash a word.

def code_word(string_):
    num_list = [random.randrange(1, 20) for i in range(0, 10)]
    string_ = string_.upper()
    coded_word = string_[0]
    for char in string_[1: len(string_)]:
        coded_word += str(num_list[random.randint(min(range(len(num_list))), max(range(len(num_list))))])
    return coded_word

code_word("Test")

# 75. Write a Python program to get the copyright information.

print(sys.copyright)

# 76. Write a Python program to get the command-line arguments (name of the script, 
# the number of arguments, arguments) passed to a script.

# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.
# 78. Write a Python program to find the available built-in modules.
# 79. Write a Python program to get the size of an object in bytes.
# 80. Write a Python program to get the current value of the recursion limit.

# 81. Write a Python program to concatenate N strings.

list_of_colors = ['Red', 'White', 'Black']
"-".join(list_of_colors)

# 82. Write a Python program to calculate the sum over a container.

sum([10, 15, 29])

# 83. Write a Python program to test whether all numbers of a list is greater than a certain number.

# Solution 1:

threshold = int(input("Please type your threshold: "))
lst = [10, 20, 30, 40, 50]
result = list(filter(lambda x: x > threshold , lst))
print(True if len(result) == len(lst) else False)

# Solution 2:

all(x > threshold for x in lst)
all(x > 5 for x in lst)

# 84. Write a Python program to count the number occurrence of a specific character in a string.

input("Please type a word: ").count(input("Number of ocurrence for a specific character: "))

# 85. Write a Python program to check whether a file path is a file or a directory.

os.path.exists(r"..../solutions_four.py")

# 86. Write a Python program to get the ASCII value of a character. 

char = input("Please type a character: ")
print("The ascii value of '" + char + "' is", ord(char))

# 87. Write a Python program to get the size of a file.

print(os.path.getsize(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py"), "Bytes")

# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50".

# Solution 1:

def num_add(x, y):
    print("{}+{}={}".format(x, y, x+y))

# Solution 2:

def num_add_two(x, y):
    print("%i+%i=%i"%(x, y, x+y))

num_add(30, 20)
num_add_two(30, 20)

# 89. Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" 
# and do nothing if the value is not equal.

variable = int(input("Please type a value: "))
if variable == 1:
    print("First day of a Month")

# 90. Write a Python program to create a copy of its own source code.
# 91. Write a Python program to swap two variables.

def swap(x, y):
    temp = x
    x = y
    y = temp
    print("x was", y, "then became", x, "\ny was", x, "then became", temp)

swap(5,10)

# 92. Write a Python program to define a string containing special characters in various forms.

print("""Tunahan""")
print('Tunahan')
print("Tuna""han")
print(r"Tunahan")

# 93. Write a Python program to get the identity of an object.

obj = object()
id(obj)

# 94. Write a Python program to convert a byte string to a list of integers.

variable = b"Tunahan"
list(variable)

# 95. Write a Python program to check whether a string is numeric.

try:
    float(input("Please type something: "))
except ValueError:
    print("It is not numeric.")

# 96. Write a Python program to print the current call stack.
# 97. Write a Python program to print the current call stack.
# sorted(set(globals().keys()) | set(__builtins__.__dict__.keys()) - set('_ names i'.split()))

# 98. Write a Python program to get the system time. Go to the editor
# Note : The system time is important for debugging, network information, 
# random number seeds, or something as simple as program performance.

time.ctime()

# 99. Write a Python program to clear the screen or terminal.

os.system("cls")
time.sleep(2)

# 100. Write a Python program to get the name of the host on which the routine is running.
# 101. Write a Python program to access and print a URL's content to the console.
# 102. Write a Python program to get system command output.
# 103. Write a Python program to extract the filename from a given path.

os.path.split(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py")[1]
os.path.basename(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py")

# 104. Write a Python program to get the effective group id, effective user id, real group id,
# a list of supplemental group ids associated with the current process.
# Note: Availability: Unix.
# 105. Write a Python program to get the users environment.

os.environ

# 106. Write a Python program to divide a path on the extension separator.

os.path.split(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py")
os.path.splitext(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py")

# 107. Write a Python program to retrieve file properties.

time.ctime(os.path.getatime(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py"))
time.ctime(os.path.getctime(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py"))
time.ctime(os.path.getmtime(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py"))
os.path.getsize(r"C:\Users\Ezgi\Desktop\Tunahan Abimin Klasörü/solutions_four.py")

# 108. Write a Python program to find path refers to a file or directory when you encounter a path name.
# 109. Write a Python program to check if a number is positive, negative or zero.

print("Positive" if int(input("Please type a number: ")) > 0 else "Negative or zero")

# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

def divisible_numbers():
    lst = []
    while True:
        try:
            int_input = int(input('Please type a number. If you want to stop adding, please type any letter: '))
            lst.append(int_input)
        except ValueError:
            print("Please do not type something other than number.")
            break
    return list(filter(lambda num: num % 15 == 0, lst))

divisible_numbers()

# 111. Write a Python program to make file lists from current directory using a wildcard.

file_list = glob.glob("*.*")
print(file_list)

# 112. Write a Python program to remove the first item from a specified list.

lst = divisible_numbers()
print(lst)
lst.pop()
print(lst)

# 113. Write a Python program to input a number, if it is not a number generate an error message.

while True:
    try:
        value_ = int(input("Please type a number: "))
    except ValueError:
        print("Error. It is not an integer.")
        break

# 114. Write a Python program to filter the positive numbers from a list.

list(filter(lambda num: num > 0, lst))

# 115. Write a Python program to compute the product of a list of integers (without using for loop).

lst = [1, 2, 3, 4, 5]
product_list = reduce(lambda x, y: x * y, lst)
result_smallest = reduce(lambda x, y: x if x < y else y, lst)
result_greatest = reduce(lambda x, y: x if x > y else y, lst)

# 116. Write a Python program to print Unicode characters.
# 117. Write a Python program to prove that two string variables of same value point same memory location.

str1 = "Tunahan"
str2 = "Tunahan"

hex(id(str1))
hex(id(str2))

# 118. Write a Python program to create a bytearray from a list.
# 119. Write a Python program to display a floating number in specified numbers.

print("%f"%100.066312)
print("%.2f"%100.066312)
print("%.3f"%100.066312)

# 120. Write a Python program to format a specified string to limit the number of characters to 6.

# Solution 1:

str_inp = input("Please type something: ")
if len(str_inp) <= 6:
    print(str_inp)
else:
    print(str_inp[:6])

# Solution 2:

print("%.6s"%str_inp)

# 121. Write a Python program to determine whether variable is defined or not.

try:
    var1 = 1
except NameError:
    print("Variable is not defined.")
else:
    print("Variable is defined.")

try:
    var2
except NameError:
    print("Variable is not defined.")
else:
    print("Variable is defined.")

# 122. Write a Python program to empty a variable without destroying it.
# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}

# 123. Write a Python program to determine the largest and smallest integers, longs, floats.
# 124. Write a Python program to check whether multiple variables have the same value.

var1 = "Tuna"
var2 = "Tuna"
var3 = "Tuna"

if var1 == var2 == var3:
    print("All variables have the same value.")
else:
    print("All variables do not have the same value.")

# 125. Write a Python program to sum of all counts in a collections?

lst = [1,2,3,4,5,6,7,8,9]
print(len(lst))

# 126. Write a Python program to get the actual module object for a given object.
# 127. Write a Python program to check whether an integer fits in 64 bits.
# 128. Write a Python program to check whether lowercase letters exist in a string.

txt_ = "Tunahan"
txt_2 = "TUNAHAN"
print(any([char.islower() for char in txt_]),
          any([char.islower() for char in txt_2]), sep="\n")

# 129. Write a Python program to add trailing and leading zeroes to a string.
# 130. Write a Python program to use double quotes to display strings.

print(json.dumps({"Tunahan": 100, "Batuhan": 100, "Ali": 100}))

# 131. Write a Python program to split a variable length string into variables.
# 132. Write a Python program to list home directory without absolute path.
# 133. Write a Python program to calculate the time runs
# (difference between start and current time) of a program.

start = datetime.now()
finish = datetime.now()

(finish - start).seconds

# 134. Write a Python program to input two integers in a single line.

inp1 = 5
inp2 = 6
str("%i%i"%(inp1, inp2))

# 135. Write a Python program to print a variable without spaces between values.
# Sample value : x =30
# Expected output : Value of x is "30"

inp = input("Sample value : x =")
print('Expected output : Value of x is "{}"'.format(inp))

# 136. Write a Python program to find files and skip directories of a given directory.
# 137. Write a Python program to extract single key-value pair of a dictionary in variables.

d = {"Tunahan": "Statistics"}
(char1, char2), = d.items()

# 138. Write a Python program to convert true to 1 and false to 0.

inp = input("Please type something: ").lower()
print(1 if inp == "true" else (0 if inp == "false" else "Error."))

# 139. Write a Python program to valid a IP address.

# 140. Write a Python program to convert an integer to binary keep leading zeros.
# Sample data : x=12
# Expected output : 00001100
# 1100

num = 8
print(format(num, "08b"))
print(format(num, "010b"))

# 141. Write a python program to convert decimal to hexadecimal.
# Sample decimal number: 30, 4
# Expected output: 1e, 04
# 142. Write a Python program to find the operating system name, platform and platform release date.
# 143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.
# 144. Write a Python program to check whether variable is of integer or string.

int_ = 5
isinstance(int_, int)

# 145. Write a Python program to test if a variable is a list or tuple or a set.

isinstance(int_, list)
isinstance(int_, tuple)
isinstance(int_, set)

# 146. Write a Python program to find the location of Python module sources.
# 147. Write a Python function to check whether a number is divisible by another number. 
# Accept two integers values form the user.

lst = []
while True:
    try:
       inp = int(input("Please type a number: "))
       lst.append(inp)
    except ValueError:
        print("Please do not type something other than integer.")
        continue
    if len(lst) == 2:
        break

divided_by = int(input("Please type a number to divide: "))
print([str(i)+" is divisible by "+str(divided_by) if i % divided_by == 0 else str(i)+" is not divisble" for i in lst])

# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
# Note: Do not use built-in functions.

# Solution 1:

lst = [10, 20, 5, 50, 123, 523]
print("Minimum is :"+str(reduce(lambda x, y: x if x < y else y, lst)),
      "Maximum is :"+str(reduce(lambda x, y: x if x > y else y, lst)), sep="\n")

# 149. Write a Python function that takes a positive integer and 
# returns the sum of the cube of all the positive integers smaller than the specified number.

while True:
    try:
        inp = int(input("Please type a number: "))
        break
    except ValueError:
        print("Please do not type something other than integer.")
        continue
    if inp < 0:
        print("Please only type a positive integer.")
        break

num = 0
for i in range(0, inp):
    num += i**3
print(num)





