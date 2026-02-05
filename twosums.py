# Hashmap
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s ={}
        for i, elem in enumerate(nums):
            needed_value = target - elem
            if needed_value in s:
                return [s[needed_value], i]
            s[elem] = i