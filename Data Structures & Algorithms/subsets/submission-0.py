class Solution:
    def _subsets(self, nums: List[int], index: int) -> List[List[int]]:
        if index == -1:
            return [[]]
        prev = self._subsets(nums, index - 1)
        res = []
        for soln in prev:
            res.append(soln + [nums[index]])
        return prev + res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: 6 minutes
        """
        return self._subsets(nums, len(nums) - 1)