class Solution:
    def _combinationSum_most_rec(self, candidates: List[int], target: int, index: int, combo: List[int]) -> List[List[int]]:
        if target == 0:
            return [combo.copy()]
        if index == len(candidates) or target < 0:
            return []
        res = []
        res += self. _combinationSum_most_rec(candidates, target, index + 1, combo)
        new_target = target - candidates[index]
        combo.append(candidates[index])
        res += self. _combinationSum_most_rec(candidates, new_target, index, combo)
        combo.pop()
        return res

    def _combinationSum_more_rec(self, candidates: List[int], target: int, index: int, combo: List[int]) -> List[List[int]]:
        if target == 0:
            return [combo.copy()]
        if index == len(candidates):
            return []
        res = []
        res += self. _combinationSum_more_rec(candidates, target, index + 1, combo)
        new_target = target - candidates[index]
        to_backtrack = 0
        while new_target >= 0:
            combo.append(candidates[index])
            res += self. _combinationSum_more_rec(candidates, new_target, index + 1, combo)
            new_target -= candidates[index]
            to_backtrack += 1
        # Backtrack until all added items to combo are removed
        for _ in range(to_backtrack):
            combo.pop()
        return res

    def _combinationSum(self, candidates: List[int], target: int, index: int, combo: List[int]) -> List[List[int]]:
        if target == 0:
            return [combo.copy()]
        if index == len(candidates):
            return []
        res = []
        for i in range(index, len(candidates)):
            candidate = candidates[i]
            new_target = target - candidate
            to_backtrack = 0
            while new_target >= 0:
                combo.append(candidate)
                res += self._combinationSum(candidates, new_target, i + 1, combo)
                new_target -= candidate
                to_backtrack += 1
            # Backtrack until all added items to combo are removed
            for _ in range(to_backtrack):
                combo.pop()
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: 20 min
        """
        candidates.sort(reverse=True) # Sorting in reverse allows us to prune the search space better and exit out of situations earlier when curr sum > target. e.g. it's better to exit earlier by adding a 11 and a 3 when the sum is 13, rather than recursing down four 3s and then adding an 11 to see that the sum has overflown.
        return self._combinationSum(candidates, target, 0, [])