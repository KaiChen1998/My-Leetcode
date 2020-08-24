class Solution:
    def __init__(self):
        """
        Key points:
            1. 不仅是你能到他，他也得能到你
            2. 注意排除已经访问的结点
        
        """
        self.directions = {1: [(0, -1), (0, 1)],
                        2: [(1, 0), (-1, 0)],
                        3: [(0, -1), (1, 0)], 
                        4: [(1, 0), (0, 1)],
                        5: [(0, -1), (-1, 0)],
                        6: [(0, 1), (-1, 0)] 
                        }

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        """
        access: visiting history table
        {-2: not vistied, -1: visited but no result, 0 / 1: can/can't go to destination}
        """
        self.m, self.n = len(grid), len(grid[0])
        access = [[-2 for _ in range(self.n)] for _ in range(self.m)]
        return self.dfs(grid, access, 0, 0)

    def accessiable(self, grid, x, y, a, b):
        # (x, y) can actually access to (a, b)
        if(not (0 <= x and x < self.m and 0 <= y and y < self.n)):
            return False
        return (a, b) in [(x + each[0], y + each[1]) for each in self.directions[grid[x][y]]]

    def dfs(self, grid, access, x, y):
        if(x == self.m - 1 and y == self.n - 1): # destination
            return True
        
        access[x][y] = -1 if access[x][y] == -2 else access[x][y] # not visit again
        directions = [(x + each[0], y + each[1]) for each in self.directions[grid[x][y]] if self.accessiable(grid, x + each[0], y + each[1], x, y) and access[x + each[0]][y + each[1]] != -1]
        for each in directions:
            if(access[each[0]][each[1]] == -2): # unvisited
                access[each[0]][each[1]] = self.dfs(grid, access, each[0], each[1])
            if(access[each[0]][each[1]] == False):
                continue
            else:
                return True
        return False