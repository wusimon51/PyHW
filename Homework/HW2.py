import random

# YOUR NAME HERE

'''
Problem 1
Implement calculate_tax to compute the price of an item after tax is applied to it. New York's tax rate
is 8.875%. You also need to round your final answer to two decimal places, and that can be done using the round() 
function. It is used as round(num, digits), where num is the number to round and digits is the number of decimal
places to round to. For instance, round(1.2348, 3) returns 1.235.
'''


def calculate_tax(price):
    return None


'''
Problem 2
Write a function named compute_hypotenuse that takes in two ints a, b in a right triangle and computes the length of the
hypotenuse.
'''


def compute_hypotenuse(a, b):
    return None

'''
Problem 3
Write a function called distance that returns the Euclidean distance between two points. Its parameters should be 
x1, y1, x2, and y2. You should look up the distance formula if you forgot or don't know what it is. To test if your 
function works, I wrote a function that uses the distance formula to approximate pi. Uncomment my code, and if your 
function is correct, then you should get at least 3.141 plus or minus 0.001. 
'''


def distance(x1, y1, x2, y2):
    return None


# def monteCarlo(numPoints):
#     insideCount = 0
#     for point in range(numPoints):
#         x = random.uniform(0, 1)
#         y = random.uniform(0, 1)
#         if distance(x, y, 0, 0) <= 1:
#             insideCount += 1
#     return 4 * insideCount / numPoints
#
# sum = 0
# for x in range(10):
#     sum += monteCarlo(100000)
# print(sum / 10)

'''
Problem 4
Write a function that determines whether a year is a leap year. There are two rules: the year has to be divisible by
4, unless it is a multiple of 100, where only years divisible by 400 are leap years. So, 2000 and 1992 are leap years, 
but 1900 is not.
'''


def is_leap_year(year):
    return None
