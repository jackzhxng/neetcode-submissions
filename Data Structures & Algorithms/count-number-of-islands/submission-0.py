class Solution:
    def exploreIsland(self, grid: List[List[str]], r: int, c: int, visited: set[Tuple[int, int]]) -> None:
        if (r, c) in visited:
            return
        visited.add((r, c))
        if r + 1 < len(grid) and grid[r + 1][c] == "1":
            self.exploreIsland(grid, r + 1, c, visited)
        if r - 1 > -1 and grid[r - 1][c] == "1":
            self.exploreIsland(grid, r - 1, c, visited)
        if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
            self.exploreIsland(grid, r, c + 1, visited)
        if c - 1 > -1 and grid[r][c - 1] == "1":
            self.exploreIsland(grid, r, c - 1, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time taken: 16 min
        """
        num_islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                if (i, j) in visited:
                    continue
                self.exploreIsland(grid, i, j, visited)
                num_islands += 1
        return num_islands