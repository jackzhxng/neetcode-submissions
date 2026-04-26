from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time taken: 16 mins
        """
        num_oranges = 0
        queue = deque()
        seen = set()
        # Count oranges and rotten oranges.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    num_oranges += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
                    seen.add((i, j))
        if num_oranges == 0:
            return 0

        # BFS
        waves = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = 2
                for offset_i, offset_j in [
                    (0, 1),
                    (1, 0),
                    (-1, 0),
                    (0, -1),
                ]:
                    if (
                        i + offset_i > -1
                        and i + offset_i < len(grid)
                        and j + offset_j > -1
                        and j + offset_j < len(grid[0])
                    ):
                        new_i, new_j = i + offset_i, j + offset_j
                        if grid[new_i][new_j] == 1 and (new_i, new_j) not in seen:
                            queue.append((new_i, new_j))
                            seen.add((new_i, new_j))
            waves += 1
        
        return waves if len(seen) == num_oranges else -1
                        

                
