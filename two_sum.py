class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    break
                test = nums[i] + nums[j]
                if test == target:
                    return [i, j]
