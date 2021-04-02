# Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input:
# strs = ["apt","pat","ear","tap","are","arm"]

# Output:
# [["apt","pat","tap"],["ear","are"],["arm"]]
# Example 2:

# Input:
# strs = [""]

# Output:
# [[""]]
# Example 3:

# Input:
# strs = ["a"]

# Output:
# [["a"]]
def csGroupAnagrams(strs):
    if len(strs) == 0:
        return None
    result = []
    queue = []
    strsComp = ""
    while len(strs) > 0:
        value = strs.pop(0)
        strsComp += value
        sub_st_sort = sorted(value)
        if len(strs) == 0:
            queue.append(value)
            result.append(queue)
            queue = []
            strsComp = ""
            break
        
        j = 0
        while j < len(strs):
            sub_string = sorted(strs[j])
            if len(queue) == 0:
                queue.append(strsComp)
            if sub_st_sort == sub_string:
                if value not in queue:
                    queue.append(value)
                queue.append(strs[j])
                strs.pop(j)
                j -= 1
            j += 1
            
           
        result.append(queue)
        queue = []

        strsComp = ""
    if len(result) >1:
        result = sorted(result, key = len, reverse = True)
    return result


strs = ["apt", 
 "pat", 
 "ear", 
 "tap", 
 "are", 
 "arm"]       
csGroupAnagrams(strs)