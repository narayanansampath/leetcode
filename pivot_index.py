# https://leetcode.com/problems/find-pivot-index/
# difficulty: easy
# tags: prefix

# problem
# Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

from typing import List

class Solution:
    def sumRange(self, left: int, right: int) -> int:
        sum_result = self.prefix_sum[right+1] - self.prefix_sum[left]
        return sum_result

    def pivotIndex(self, nums: List[int]) -> int:
        currSum = 0
        self.prefix_sum = [0]
        for i in nums:
            currSum += i
            self.prefix_sum.append(currSum)

        for i in range(0, len(self.prefix_sum)):
            lsum = 0
            rsum = 0
            if (i == 0):
                rsum = self.prefix_sum[i+1] - self.prefix_sum[len(nums)]
            elif (i == (len(nums))):
                lsum = self.prefix_sum[i-1]
            else:
                lsum = self.sumRange(0, i-1)
                rsum = self.sumRange(i+1, len(nums)-1)
            if lsum == rsum:
                return i
        return -1