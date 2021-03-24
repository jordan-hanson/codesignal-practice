# Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

# The Valid bracket sequence is defined in the following way:

# An empty bracket sequence is a valid bracket sequence.
# If S is a valid bracket sequence then (S), [S] and {S} are also valid.
# If A and B are valid bracket sequences then AB is also valid.
# Example

# For sequence = "()", the output should be validBracketSequence(sequence) = true;
# For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
# For sequence = "(]", the output should be validBracketSequence(sequence) = false;
# For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
# For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string sequence

# A bracket sequence, consisting of the characters (, ), [, ], {, and }.

# Guaranteed constraints:
# 0 ≤ sequence.length ≤ 106.

# [output] boolean

# true if sequence is a valid bracket sequence and false otherwise.
def validBracketSequence(sequence):
    myStack = []
    paran = "("
    brack = "["
    curly = "{"
    if len(sequence) == 0:
        return True
    if len(sequence) < 2:
        return False
    for i, element in enumerate(sequence):
        if element == "(":
            myStack.append(element)
            continue
        if element == "[":
            myStack.append(element)
            continue
        if element == "{":
            myStack.append(element)
            continue
        if i == 0 and element == "]":
            return False
            break
        if i == 0 and element == ")":
            return False
            break
        if i == 0 and element == "}":
            return False
            break
        mostRecent = myStack.pop()
        if mostRecent == paran:
            if element == ")":
                return True
            else: return False
        if mostRecent == brack:
            if element == "]":
                return True
            else: return False
        if mostRecent == curly:
            if element == "}":
                return True
            else: return False
    print(myStack)

    # Fails 1 test with input "[][{](})"