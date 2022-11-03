# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

#my solution:
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        m = (len(nums)-1)//2
        start = 0
        end = len(nums)-1
        if target <= nums[start]:
            return 0
        elif target == nums[end]:
            return end
        elif target> nums[end]:
                return end+1
        
        while end-start>1: # error i've created: end>start, this doesn't work because for sorted link, right is always larger than left so it will endup with unlimited loop.
            if nums[m]==target:
                return m
            elif nums[m] < target:
                start = m
                end = end
                m = m+(end-start)//2
            elif nums[m] > target:
                start = start
                end = m
                m = start + (end-start)//2
                
        return end

# online solution:https://www.youtube.com/watch?v=K-RYzDZkzCI
# iterate through n elements in the list, o(n)
# solution: binary search O(Log（n）)
# left pointer, right pointer, compute middle point
# PS：I was on the right track, supurise! HAHAHAHAHA