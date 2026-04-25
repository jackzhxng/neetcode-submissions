class Solution:
    def _canJump(self, nums: List[int], index: int, memo: Dict[int, bool]) -> bool:
        if index in memo:
            return memo[index]
        if index == len(nums) - 1:
            return True
        max_jumps = nums[index]
        for i in range(1, max_jumps + 1):
            if self._canJump(nums, index + i, memo):
                memo[index] = True
                return True
        memo[index] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        """
        Time: 21 minutes

        Tried top down DP with memo first, was too slow. Then tried bottom up DP, too slow as well. Settled on current solution.
        """
        # return self._canJump(nums, 0, {})

        furthest = 0
        for i in range(len(nums)):
            num = nums[i]
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
        return True
