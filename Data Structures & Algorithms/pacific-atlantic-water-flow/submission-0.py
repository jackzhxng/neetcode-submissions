class Solution:
    def maxFlow(self, heights: List[List[int]], i: int, j: int, visited: set[Tuple[int, int]]):
        if (i, j) in visited:
            return
        visited.add((i, j))
        height = heights[i][j]
        if i - 1 > -1 and heights[i - 1][j] >= height:
            self.maxFlow(heights, i - 1, j, visited)
        if i + 1 < len(heights) and heights[i + 1][j] >= height:
            self.maxFlow(heights, i + 1, j, visited)
        if j - 1 > -1 and heights[i][j - 1] >= height:
            self.maxFlow(heights, i, j - 1, visited)
        if j + 1 < len(heights[0]) and heights[i][j + 1] >= height:
            self.maxFlow(heights, i, j + 1, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time taken: 19 min
        """
        # Reverse flow from pacific
        pacific = set()
        for i in range(len(heights)):
            if (i, 0) in pacific:
                continue
            self.maxFlow(heights, i, 0, pacific)
        for j in range(len(heights[0])):
            if (0, j) in pacific:
                continue
            self.maxFlow(heights, 0, j, pacific)

        # Reverse flow from atlatic
        atlantic = set()
        for i in range(len(heights)):
            if (i, len(heights[0]) - 1) in atlantic:
                continue
            self.maxFlow(heights, i, len(heights[0]) - 1, atlantic)
        for j in range(len(heights[0])):
            if (len(heights) - 1, j) in atlantic:
                continue
            self.maxFlow(heights, len(heights) - 1, j, atlantic)
        
        return list(pacific & atlantic)

