# List-1 > first_last6
# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6

# List-1 > same_first_last
# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

# List-1 > make_pi
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# make_pi() → [3, 1, 4]
def make_pi():
  return [3,1,4]

# List-1 > common_end
# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
# Both arrays will be length 1 or more.
# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

# List-1 > sum3
# Given an array of ints length 3, return the sum of all the elements.
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7
# NOTE THAT THIS IS O(n) where as "for i in nums: sum += i return sum" is O(n)
def sum3(nums):
    return nums[0] + nums[1] + nums[2]

# List-1 > rotate_left3 HARD
# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
# rotate_left3([1, 2, 3]) → [2, 3, 1]
# rotate_left3([5, 11, 9]) → [11, 9, 5]
# rotate_left3([7, 0, 0]) → [0, 0, 7]
def rotate_left3(nums):
    return [nums[(i + 1) % len(nums)] for i in range(len(nums))]

# List-1 > reverse3
# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
# reverse3([1, 2, 3]) → [3, 2, 1]
# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]
# def reverse3(nums):
#     return nums[::-1]
def reverse3(nums):
    return nums[::-1]

# List-1 > max_end3
# Given an array of ints length 3, figure out which is larger, the first or last element in the array,
# and set all the other elements to be that value. Return the changed array.
# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]
def max_end3(nums):
    max_value = max(nums[0], nums[2-1])
    return len(nums) * [max_value]

def max_end3_v2(nums):
    if nums[0] > nums[-1]:
        return 3 * [nums[0]]
    else:
        return 3 * [nums[-1]]

# List-1 > sum2
# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
# sum2([1, 2, 3]) → 3
# sum2([1, 1]) → 2
# sum2([1, 1, 1, 1]) → 2
def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    elif len(nums) == 1:
        return nums[0]
    else:
        return 0

# List-1 > middle_way
# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
# middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
def middle_way(a, b):
    # integer division - rounds down
    mid_a = len(a) // 2
    mid_b = len(b) // 2
    return [a[mid_a], b[mid_b]]

# List-1 > make_ends
# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
# make_ends([1, 2, 3]) → [1, 3]
# make_ends([1, 2, 3, 4]) → [1, 4]
# make_ends([7, 4, 6, 2]) → [7, 2]
def make_ends(nums):
  return [nums[0], nums[-1]]

# List-1 > has23
# Given an int array length 2, return True if it contains a 2 or a 3.
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False
def has23(nums):
    for i in nums:
        if i == 2 or i == 3:
            return True
    return False

# Logic-1 > cigar_party
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)

# Logic-1 > date_fashion
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes.
# The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes.
# If either of you is very stylish, 8 or more, then the result is 2 (yes).
# With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1
def date_fashion(you, date):
    ## Check the <=2 case first, since it takes precedence
    ## over the >=8 case.
    if (you <= 2) or (date <= 2):
        return 0
    elif (you >= 8) or (date >= 8):
        return 2
    else:
        return 1

# Logic-1 > squirrel_play
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True
def squirrel_play(temp, is_summer):
    if is_summer and temp >= 60 and temp <= 100:
        return True
    elif temp >= 60 and temp <= 90:
        return True
    return False

# Logic-1 > caught_speeding
# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2

# Logic-1 > sorta_sum
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21
def sorta_sum(a, b):
    if 10 <= (a + b) <= 19:
        return 20
    return a + b

def sorta_sum2(a, b):
    return a + b if a + b > 19 or a + b < 10 else 20

# Logic-1 > alarm_clock
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'
def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 6]:  # Weekend
            return 'off'
        else:  # Weekday
            return '10:00'
    else:
        if day in [0, 6]:  # Weekend
            return '10:00'
        else:  # Weekday
            return '7:00'

# Logic-1 > love6
# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6.
# Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True
def love6(a, b):
    return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

# Logic-1 > in1to10
# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return
# True if the number is less or equal to 1, or greater or equal to 10.
# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

# Logic-1 > near_ten
# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder
# of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True
def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8









