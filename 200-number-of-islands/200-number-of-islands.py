class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        q = collections.deque()
        
        
        def bfs(r, c):
            
            visit.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if(r in range(rows) and
                       c in range(cols) and
                       grid[r][c] == "1" and
                       (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            
        '''
        
        def dfs(r, c):
            if(r not in range(rows) or
               c not in range(cols) or
               grid[r][c] == "0" or
               (r, c) in visit):
                return
            
            visit.add((r, c))
            directions = [[0, 1], [-1, 0], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        '''
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    #dfs(r,c)
                    islands += 1
        return islands
        
            