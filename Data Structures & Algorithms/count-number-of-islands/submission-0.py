from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1) # right
        ]
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    queue = deque()
                    queue.append((r, c))
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        grid[curr_r][curr_c] = '0'
                        for dr, dc in directions:
                            nr = curr_r + dr
                            nc = curr_c + dc
                            if not (0 <= nr < rows and 0 <= nc < cols):
                                continue
                            if grid[nr][nc] == '0':
                                continue
                            queue.append((nr, nc))
        return islands
                        
