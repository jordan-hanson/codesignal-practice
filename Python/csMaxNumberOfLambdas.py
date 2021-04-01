# Given a string text, you need to use the characters of text to form as many instances of the word "lambda" as possible.

# You can use each character in text at most once.

# Write a function that returns the maximum number of instances of "lambda" that can be formed.

# Example 1:

# Input: text = "mbxcdatlas"
# Output: 1
# Example 2:

# Input: text = "lalaaxcmbdtsumbdav"
# Output: 2
# Example 3:

# Input: text = "sctlamb"
# Output: 0
# Notes:

# text consists of lowercase English characters only
# [execution time limit] 4 seconds (py3)

# [input] string text

# [output] integer
import math
from re import search
def csMaxNumberOfLambdas(text):
    input_text = text
    my_set = set()
    my_match_st = "lambda"
    new_String = ""
    count = 0
    # boolean == False
    # while boolean == False:
        # Turn True when all values have been added
    for char in my_match_st:
        print(input_text)
        if search(char, input_text):
            new_String += char
            print(new_String)
            res_str = input_text.replace(char, '')
            input_text = res_str
            print(input_text)
        # if len(my_set) == 6:
        #     count += 1
        #     my_set = set()
    # for char in my_match_st:
    #     print(char)
    #     # while new_String != my_match_st:
    #     for letter in text:
    #         if char == letter:
    #             new_String += char
    #             my_set.add(char)
    # value = math.floor(len(new_String) / 6)
    # print(value)
    print(input_text)
    print(new_String)
    # print(my_set)
    # return value