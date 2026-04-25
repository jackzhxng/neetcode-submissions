class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Time: 15 mins

        Naive bottom up DP passed but placed ~90%, added `furthest` optimization to reduce number of iterations

        There's a way to do it greedy too but it's also a bit tricky.
        """
        dp = [None for _ in range(len(nums))]
        dp[0] = 0
        furthest = 0
        for i, num in enumerate(nums):
            if dp[i] is None:
                return -1 # Shouldn't happen since it's guaranteed you can reach nums[n - 1].
            for dest in range(max(furthest, i + 1), min(len(nums), i + 1 + num)):
                if dp[dest] is None:
                    dp[dest] = dp[i] + 1
                else:
                    dp[dest] = min(dp[dest], dp[i] + 1)
                furthest = max(furthest, dest)
        return dp[-1]