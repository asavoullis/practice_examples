# Warmup-1 > sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True
def sleep_in(weekday, vacation):
    # if not weekday or vacation:
    if weekday and not vacation:
        return False
    else:
        return True


# Warmup-1 > monkey_trouble
#
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False


# Warmup-1 > sum_double
# Given two int values, return their sum.
# Unless the two values are the same, then return double their sum.
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


# Warmup-1 > diff21
# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
#
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0
def diff21(n):
    if n > 21:
        return abs(2 * (n - 21))
    else:
        return abs(n - 21)


# Warmup-1 > parrot_trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# Warmup-1 > makes10
# Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
#
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True
def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)
    # if (a == 10 or b == 10) or (a+b==10):
    #     return True
    #   else:
    #     return False


# Warmup-1 > near_hundred
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False
def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    # if abs(100-n) <= 10 or abs(200-n) <= 10:
    #     return True
    #   else:
    #     return False


# Warmup-1 > not_string
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
def not_string(str):
    if str[:3] == "not":
        return str
    return "not " + str


# Warmup-1 > missing_char
# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).
#
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'
def missing_char(str, n):
    return str[:n] + str[n+1:]


# Warmup-1 > front_back
# Given a string, return a new string where the first and last chars have been exchanged.
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'
def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


# Warmup-1 > front3
# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.
#
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'
def front3(str):
    if len(str) < 3:
        return 3 * str
    return 3 * str[:3]


# Warmup-2 > string_times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'
def string_times(str, n):
    return n * str
def string_times2(str, n):
    result = ""
    for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
        result = result + str  # could use += here
    return result

# Warmup-2 > front_times
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
def front_times(str, n):
    return n * str[:3]
def front_times2(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]
    result = ""
    for i in range(n):
        result = result + front
    return result


Warmup-2 > string_bits
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'


