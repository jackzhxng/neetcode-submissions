class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time taken: 28 min

        This is a bit more complicated version of https://leetcode.com/problems/maximum-product-subarray/solutions/3321410/c-kadanes-algo-full-explanation-by-garvi-x4oz/

        - Divide nums into subarrays separated by 0s
        - For every subarray, the max product will be either the start until somewhere in the middle, or somewhere in the middle until the end, e.g. xxxxxx----0 or -----xxx0
        - Thus we increase r until a 0, then we increase l if cum prod is negative until the sign flips
        """
        l, r = 0, 0
        max_prod = -float("inf")
        curr_prod = 1
        while r < len(nums):
            if nums[r] == 0: # End of a run
                # Increase l until curr_prod is positive, increment r, set l to r
                while curr_prod < 0 and l < r:
                    curr_prod //= nums[l]
                    l += 1
                if l < r:
                    max_prod = max(max_prod, curr_prod)
                r += 1
                l = r
                curr_prod = 1
                continue
            curr_prod *= nums[r]
            max_prod = max(max_prod, curr_prod)
            r += 1
        while curr_prod < 0 and l < r:
            curr_prod //= nums[l]
            l += 1
        if l < r:
            max_prod = max(max_prod, curr_prod)
        if 0 in nums:
            return max(0, max_prod)
        return max_prod