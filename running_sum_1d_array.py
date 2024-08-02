# https://leetcode.com/problems/running-sum-of-1d-array/
# difficulty: easy
# tags: prefix

# problem
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Solution, O(n) time, O(1) space

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for i in nums:
            sum += i
            result.append(sum)
        return result
