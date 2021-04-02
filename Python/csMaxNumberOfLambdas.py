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
    global count
    count = 0
    def findCount(input_text):
        global my_match_st
        my_match_st = "lambda"
        global new_String
        new_String = ""
        global count
        for char in my_match_st:
            print("line13", input_text)
            if search(char, input_text):
                new_String += char
                if new_String == my_match_st:
                    print(new_String)
                    new_String = ""
                    count += 1
                    print(count)
                    res_str = input_text.replace(char, '', 1)
                    input_text = res_str
                    result = findCount(input_text)
                    return count
                    print("line 24", count)
                print("line27", new_String)
                res_str = input_text.replace(char, '', 1)
                input_text = res_str
    my_res = findCount(input_text)
    return count