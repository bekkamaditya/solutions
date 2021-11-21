# https://leetcode.com/problems/maximum-subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -sys.maxint - 1
        maxPreSum = -sys.maxint - 1
        for num in nums:
            if maxPreSum > 0:
                maxPreSum = maxPreSum + num
            else:
                maxPreSum = num

            if maxPreSum > maxSum:
                maxSum = maxPreSum

        return maxSum
