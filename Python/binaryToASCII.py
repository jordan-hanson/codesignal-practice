# Given a binary string (ASCII encoded), write a function that returns the equivalent decoded text.

# Every eight bits in the binary string represents one character on the ASCII table.

# Examples:

# csBinaryToASCII("011011000110000101101101011000100110010001100001") -> "lambda"
# 01101100 -> 108 -> "l"
# 01100001 -> 97 -> "a"
# 01101101 -> 109 -> "m"
# 01100010 -> 98 -> "b"
# 01100100 -> 100 -> "d"
# 01100001 -> 97 -> "a"
# csBinaryToASCII("") -> ""
# Notes:

# The input string will always be a valid binary string.
# Characters can be in the range from "00000000" to "11111111" (inclusive).
# In the case of an empty input string, your function should return an empty string.
# [execution time limit] 4 seconds (py3)

# [input] string binary

# [output] string
def csBinaryToASCII(binary):
    i = 0
    new_string = ""
    while i < len(binary):
        sub_string = binary[i:i+8]
        result = chr(int(sub_string, 2))
        new_string += result
        i += 8
    print(new_string)
    return new_string
csBinaryToASCII("0100100001100101011011000110110001101111")