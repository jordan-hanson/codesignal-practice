# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# first_not_repeating_character(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# first_not_repeating_character(s) = '_'.

# There are no characters in this string that do not repeat.

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string that contains only lowercase English letters.

# [output] char

# The first non-repeating character in s of '_' if there are no characters that do not repeat.
from collections import Counter
def first_not_repeating_character(s):
# use a set for unique characters
# or use a count of each character. if only 1 return character
# else return "_"
    count = Counter(s)
    returnchar = ""
    boolean = False
    for num in count:
        if count[num] == 1:
            returnchar += num
            boolean = True
            break
    if boolean == False:
        returnchar = "_"
    return returnchar