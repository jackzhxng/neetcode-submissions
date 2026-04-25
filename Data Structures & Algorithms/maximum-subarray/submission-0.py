class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        max_sum = prev
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i])
            max_sum = max(prev, max_sum)
        return max_sum

            
