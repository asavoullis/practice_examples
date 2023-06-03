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
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
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
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'
def missing_char(str, n):
    return str[:n] + str[n+1:]


# Warmup-1 > front_back
# Given a string, return a new string where the first and last chars have been exchanged.
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
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'
def front3(str):
    if len(str) < 3:
        return 3 * str
    return 3 * str[:3]


# Warmup-2 > string_times
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
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


# Warmup-2 > string_bits
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'
def string_bits(str):
    return str[0:len(str):2]


# Warmup-2 > string_splosion
# Given a non-empty string like "Code" return a string like "CCoCodCode".
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result


# Warmup-2 > last2     HARD
# Given a string, return the count of the number of times that a substring length 2 appears in the string
# and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2
def last2(input_string):
    count = 0
    last_two = input_string[-2:]

    for i in range(len(input_string) - 2):
        if input_string[i:i + 2] == last_two:
            count += 1

    return count


# Warmup-2 > array_count9
# Given an array of ints, return the number of 9's in the array.
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3
def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


# Warmup-2 > array_front9
# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False
def array_front9(nums):
    return any(num == 9 for num in nums[:4])

def array_front9_v2(nums):
    for i in range(len(nums)):
        if nums[i] == 9 and i < 4:
            return True
    return False


# Warmup-2 > array123
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i + 3] == [1, 2, 3]:
            return True
    return False

def array1232(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


# Warmup-2 > string_match  HARD
# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0
def string_match(a, b):
    # Determine the length of the shorter string
    length = min(len(a), len(b))
    # Counter for matching substrings
    count = 0
    # Iterate through the strings up to the second-to-last index
    for i in range(length - 1):
        # Compare pairs of substrings directly
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count


# String-1 > hello_name
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'
def hello_name(name):
    return "Hello " + name + "!"


# String-1 > make_abba
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'
def make_abba(a, b):
    return a + b + b + a


# String-1 > make_tags
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


# String-1 > make_out_word
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'
def make_out_word(out, word):
    return out[:len(out)/2] + word + out[len(out)/2:]


# String-1 > extra_end
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'
def extra_end(str):
    return 3*str[-2:]


# String-1 > first_two
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
# If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
# first_two('Hello') → 'He'
# first_two('abcdefg') → 'ab'
# first_two('ab') → 'ab'
def first_two(str):
    return str[:2]


# String-1 > first_half
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'
def first_half(str):
    return str[:len(str)/2]


# String-1 > without_end
# Given a string, return a version without the first and last char, so "Hello" yields "ell".
# The string length will be at least 2.
# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'
def without_end(str):
    return str[1:len(str)-1]


# # String-1 > combo_string
# # Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
# # and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
# # combo_string('Hello', 'hi') → 'hiHellohi'
# # combo_string('hi', 'Hello') → 'hiHellohi'
# combo_string('aaa', 'b') → 'baaab'
def combo_string(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b

def combo_string2(a, b):
    if len(a) >= len(b):
      big,short = a,b
    else:
      big,short = b,a
    return short + big + short


# String-1 > non_start
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'
def non_start(a, b):
    return a[1:] + b[1:]


# String-1 > left2
# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'
def left2(str):
    if len(str) >= 2:
        return str[2:] + str[:2]
    else:
        return str







