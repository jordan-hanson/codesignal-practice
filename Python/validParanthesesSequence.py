# You are given a parentheses sequence, check if it's regular.

# Example

# For s = "()()(())", the output should be
# validParenthesesSequence(s) = true;
# For s = "()()())", the output should be
# validParenthesesSequence(s) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string, consisting only of '(' and ')'.

# Guaranteed constraints:
# 0 ≤ s.length ≤ 105.

# [output] boolean

# true is the sequence is regular and false otherwise.
def validParenthesesSequence(s):
    count = 0
    for i, e in enumerate(s):
        if count == -1:
            return False
        if e == "(":
            count += 1
        if e == ")":
            count -= 1
    print(count)
    if count == 0:
        return True
    else:
        return False

a = "()()()(("
validParenthesesSequence(a)