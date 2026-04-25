class Solution:
    digit_map = {
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    }

    def _letterCombinations(self, digits: str, index: int) -> List[str]:
        if index == -1:
            return [""]
        prev_combos = self._letterCombinations(digits, index - 1)
        res = []
        for prev_combo in prev_combos:
            for letter in self.digit_map[int(digits[index])]:
                res.append(prev_combo + letter)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time: 7 mins
        """
        if not digits:
            return []
        return self._letterCombinations(digits, len(digits) - 1)