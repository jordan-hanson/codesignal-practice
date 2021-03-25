# You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

# Write a function that returns the target value's index. If the target value is not present in the array, return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# [execution time limit] 4 seconds (py3)

# [input] array.integer nums

# [input] integer target

# [output] integer

def findValueSortedShiftedArray(nums, target):
    min_index = 0
    max_index = len(nums) -1
    while min_index <= max_index:
        mid_idx = target
        print("mid_idx", mid_idx)
        print("Middle value", nums[mid_idx])
        if target == mid_idx:
            print("mid index in target if", mid_idx)
            return nums[mid_idx]
        elif nums[mid_idx] < target:
            min_index = mid_idx + 1
            print("mid_idx in elf", mid_idx)
        else:
            max_index = mid_idx - 1
            print("max_index", max_index)
