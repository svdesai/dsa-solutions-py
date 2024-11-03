# Leetcode Problem 169: Majority Element
# Description: Given an array of size n, find the majority element that appears more than n/2 times.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count += (-1)
        return candidate
