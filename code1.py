class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        outputDict = {}
        for i in range(0, len(nums)):
            if nums[i] in outputDict:
                return [outputDict[nums[i]], i]
            else:
                outputDict[target - nums[i]] = i

