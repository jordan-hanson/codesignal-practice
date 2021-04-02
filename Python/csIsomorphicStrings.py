# Given two strings a and b, determine if they are isomorphic.

# Two strings are isomorphic if the characters in a can be replaced to get b.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# Example 1:

# Input: 
# a = "odd"
# b = "egg"

# Output:
# true
# Example 2:

# Input:
# a = "foo"
# b = "bar"

# Output:
# false
# Example 3:

# Input:
# a = "abca"
# b = "zbxz"

# Output:
# true
# Example 4:

# Input:
# a = "abc"
# b = ""

# Output:
# false
MAX_CHARS = 256
def csIsomorphicStrings(a, b):
    a_string = len(a)
    print(a_string)
    b_string = len(b)
    print(b_string)
    if a_string != b_string:
        return False
        
    visited = [False] * MAX_CHARS
    
    map = [-1] * MAX_CHARS

    for i in range(len(b)):
        if map[ord(a[i])] == -1:
            if visited[ord(b[i])] == True:
                return False
            visited[ord(b[i])] = True
            map[ord(a[i])] = b[i]
            
        elif map[ord(a[i])] != b[i]:
            return False
            
    return True