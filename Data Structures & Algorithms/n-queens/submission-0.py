class Solution:
    def _populateAttackSpace(self, attack_grid: List[List[int]], r: int, c: int, reverse: bool = False) -> void:
        # Horizontal
        for j in range(len(attack_grid[0])):
            attack_grid[r][j] += -1 if reverse else 1
        # Vertical
        for i in range(len(attack_grid)):
            attack_grid[i][c] += -1 if reverse else 1
        # Diagonal, tril
        i = 1
        while r + i < len(attack_grid) and c + i < len(attack_grid[0]):
            attack_grid[r + i][c + i] += -1 if reverse else 1
            i += 1
        i = 1
        while r - i > -1 and c - i > -1:
            attack_grid[r - i][c - i] += -1 if reverse else 1
            i += 1
        # Diagonal, triu
        i, j = 1, 1
        while r + i < len(attack_grid) and c - j > -1:
            attack_grid[r + i][c - j] += -1 if reverse else 1
            i += 1
            j += 1
        i, j = 1, 1
        while r - i > -1 and c + j < len(attack_grid[0]):
            attack_grid[r - i][c + j] += -1 if reverse else 1
            i += 1
            j += 1

    def _solveNQueens(
        self,
        grid: List[List[str]],
        attack_grid: List[List[int]],
        curr_queens: int,
        r: int,
        c: int,
    ) -> List[List[str]]:
        """
        Returns a list of 2D board configurations, hence the 3D list.
        """
        n = len(grid)
        if curr_queens == n:
            return [["".join(row) for row in grid]]
        res = []
        for i in range(r, len(grid)):
            valid = False
            for j in range(len(grid[0])):
                if attack_grid[i][j] > 0:
                    continue
                valid = True
                grid[i][j] = "Q"
                self._populateAttackSpace(attack_grid, i, j)
                res += self._solveNQueens(grid, attack_grid, curr_queens + 1, i + 1, j)
                self._populateAttackSpace(attack_grid, i, j, reverse=True)
                grid[i][j] = "."
            if not valid:
                return []
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Time: 45 mins

        - Is the right idea, although instead of incrementing/decrementing an entire attack grid
        it would be faster / easier to code to keep sets.
        - Easier to think that "each row has one queen"
        """
        grid = [["." for _ in range(n)] for _ in range(n)]
        attack_grid = [[0 for _ in range(n)] for _ in range(n)]
        r, c = 0, 0
        return self._solveNQueens(grid, attack_grid, 0, r, c)