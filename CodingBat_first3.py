# Logic-2 > make_bricks HARD
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True
def make_bricks(small, big, goal):
    big_needed = min(big, goal // 5)  # Calculate the maximum number of big bricks needed
    small_needed = goal - big_needed * 5  # Calculate the remaining length to be filled with small bricks

    return small_needed <= small  # Check if there are enough small bricks available

# Logic-2 > lone_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0
def lone_sum(a, b, c):
    if a == b == c:  # If all three values are the same
        return 0
    elif a == b:  # If a and b are the same
        return c
    elif a == c:  # If a and c are the same
        return b
    elif b == c:  # If b and c are the same
        return a
    else:  # All three values are different
        return a + b + c

# Logic-2 > lucky_sum
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
# So for example, if b is 13, then both b and c do not count.
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    else:
        return a + b + c

# Logic-2 > no_teen_sum  HARD
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive --
# then that value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if 13 <= n <= 14 or 17 <= n <= 19:
        return 0
    else:
        return n

# Logic-2 > round_sum
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
# Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times.
# Write the helper entirely below and at the same indent level as round_sum().
# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    # finding remainder using %
    if num % 10 >= 5:
        # floor division
        return (num // 10 + 1) * 10
    else:
        return (num // 10) * 10


# Logic-2 > close_far
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True
def close_far(a, b, c):
    return (abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2) or \
           (abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2) or \
           (abs(b - c) <= 1 and abs(b - a) >= 2 and abs(c - a) >= 2)

# Logic-2 > make_chocolate
# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2
def make_chocolate(small, big, goal):
    big_needed = min(big , goal /5)
    small_needed = goal - (big_needed * 5 )
    if small_needed <= small:
        return small_needed
    else:
        return -1

# String-2 > double_char
# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'
def double_char(str):
    result = ""
    for i in range(len(str)):
        result += 2 * str[i]
    return result

def double_char_v2(str):
    str2 = []
    for c in str:
        str2.append(2 * c)

    return "".join(str2)

# String-2 > count_hi
# Return the number of times that the string "hi" appears anywhere in the given string.
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2
def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i:i+2] == "hi":
            count += 1
    return count

# String-2 > cat_dog
# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True
def cat_dog(str): #FASTER
    count = 0
    for i in range(len(str)):
        if str[i:i + 3] == "dog":
            count += 1
        elif str[i:i + 3] == "cat":
            count -= 1
        else:
            continue

    if count == 0:
        return True
    else:
        return False

def cat_dog(string):
    cat_count = string.count('cat')
    dog_count = string.count('dog')
    return cat_count == dog_count

# String-2 > end_other
# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)

def end_other_v2(a, b):
    a = a.lower()
    b = b.lower()
    len_a = len(a)
    len_b = len(b)

    # Check if b appears at the very end of a
    if len_a >= len_b and a[len_a - len_b:] == b:
        return True
    # Check if a appears at the very end of b
    if len_b >= len_a and b[len_b - len_a:] == a:
        return True
    return False

# String-2 > xyz_there
# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True
def xyz_there(str):
    for i in range(len(str) - 2 ):
        if str[i:i+3] == "xyz":
            if i == 0 or str[i-1] != ".":
                return True
    return False

# List-2 > count_evens
# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0
def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1
    return count

# List-2 > big_diff
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8
def big_diff(nums):
    return max(nums) - min(nums)

# List-2 > centered_average
# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.
# If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
# You may assume that the array is length 3 or more.
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3
def centered_average(nums):
    min_value = min(nums)
    max_value = max(nums)
    average = 0

    nums.remove(min_value)
    nums.remove(max_value)
    for i in nums:
        average += i
    average = average / len(nums)
    return average

def centered_average(nums):
    nums.sort()  # Sort the array in ascending order
    sum = 0
    for i in range(1, len(nums) - 1):  # Exclude the first and last elements
        sum += nums[i]
    return sum // (len(nums) - 2)  # Calculate the centered average using integer division

# List-2 > sum13
# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6
def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if i == 0 and nums[i] != 13:
            sum += nums[i]

        elif nums[i] == 13 or (nums[i - 1] == 13):
            continue
        else:
            sum += nums[i]
    return sum

def sum13(nums):
    sum = 0
    skip_next = False
    for num in nums:
        if skip_next:
            skip_next = False
            continue
        if num == 13:
            skip_next = True
            continue
        sum += num
    return sum

# List-2 > sum67
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
# (every 6 will be followed by at least one 7). Return 0 for no numbers.
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4
def sum67(nums):
    sum = 0
    skip_next = False
    for num in nums:
        if num == 6:
            skip_next = True
            continue
        if num == 7 and skip_next:
            skip_next = False
            continue
        if not skip_next:
            sum += num
    return sum

# List-2 > has22
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True

    return False
