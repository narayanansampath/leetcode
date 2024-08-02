# https://leetcode.com/problems/range-sum-query-immutable/
# difficulty: easy
# tags: prefix

# problem
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        currSum = 0
        self.prefix_sum = [0]
        for i in nums:
            currSum += i
            self.prefix_sum.append(currSum)

    def sumRange(self, left: int, right: int) -> int:
        sum_result = self.prefix_sum[right+1] - self.prefix_sum[left]
        return sum_result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray([1,2, 23, ,4 ])
# param_1 = obj.sumRange(left,right)