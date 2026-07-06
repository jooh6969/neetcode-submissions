from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0
        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1) # right
        ]
        # Remember to mark visited right after appending, 
        # otherwise there may be multiple appends
        # triangle graph is the easiest example
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                curr_area = 0
                queue = deque()
                queue.append((r, c))
                grid[r][c] = 0 
                while queue:
                    curr_r, curr_c = queue.popleft()
                    curr_area += 1
                    for dr, dc in directions:
                        nr = curr_r + dr
                        nc = curr_c + dc
                        if not(0 <= nr < rows and 0 <= nc < cols):
                            continue
                        if grid[nr][nc] == 1:
                            queue.append((nr, nc))
                            grid[nr][nc] = 0
                area = max(area, curr_area)
        return area
                        
                        

