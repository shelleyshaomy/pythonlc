# Given an integer array nums, find the subarray which has the largest sum and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer approach,
#  which is more subtle.


# my solution O(n^3) timeout
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find all subarray
        maxsum = nums[0]
        for index in range(len(nums)):
            for i in range(index+1,len(nums)+1):
                subarray = nums[index:i]
                #print(subarray)
                subsum = sum(subarray)
                if subsum>maxsum:
                    maxsum = subsum
        return maxsum

# solution:https://www.youtube.com/watch?v=7J5rs56JBs8

# O(n^2)
class Solution:
    def maxContiguousSubarraySum(self, nums):
        '''
        :type nums: list of int
        :rtype: int
        '''
        n = len(nums)
        # Arbitrary minimum value for python
        max_sum = -1000000000

        # Left will be the starting index of subarray
        for left in range(0, n):
            running_sum = 0
            # Right will be the ending index of subarray
            for right in range(left, n):

                # Add the current element to previous computed value
                # To get the subarray sum
                running_sum += nums[right]
                
                # Does this window beat the best sum we have seen so far?
                max_sum = max(max_sum, running_sum)

        return max_sum
    

# O(n)
# consider if we have to use ith element of array:
# compare the max sum number for subarray contains i-1th, if <0, then reject, subarray start from i itself
# exp: array  [-2,1,-3,4,-1,2,1,-5,4]
#      maxfunc[-2,1,-2,4,3, 5,6,1,6]
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find all subarray
        maxmum = nums[0]
        leftmax = nums[0]
        for i in range(1,len(nums)):
            leftmax = max(nums[i],leftmax + nums[i])
            maxmum = max(leftmax, maxmum)
        
        return maxmum

