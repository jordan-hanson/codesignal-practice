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

    result = []
    queue = []
    strsComp = ""
    if len(strs) >= 1:
        print(strs)
        for i, value in enumerate(strs):
            strsComp += value
            sub_st_sort = sorted(value)
            print("strs", strs)
            if len(strs) == 1:
                print("hit it")
                oneL = queue.append(i)
                result.append(queue)
                queue = []
                strsComp = ""
                break
            for j, v in enumerate(strs):
                print("line 20", v)
                sub_string = sorted(v)
                print(sub_string)
                print(strs)
                print(len(strs))
                if len(strs) == 1:
                    queue.append(value)
                if len(queue) == 0:
                    queue.append(strsComp)
                if sub_st_sort == sub_string:
                    queue.append(v)
                    print(strs[j])
                    strs.pop(j)
            if len(strs) == 0:
                strs.pop(i)
                strsComp = ""
            result.append(queue)
            queue = []
            strs.pop(i)
            strsComp = ""
            print("35", result)