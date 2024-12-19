class Solution:
    def readFile(self, filename):
        grid = []
        
        with open(filename) as file:
            for line in file:
                grid.append(list(map(int, list(line.strip()))))

        return grid
    
    def solution1(self, filename):
        grid = self.readFile(filename)
        
        def dfs(grid, row, col, trailends):
            height = grid[row][col]
            if height == 9:
                res = (row, col) not in trailends
                trailends.add((row, col))
                return int(res)
            
            res = 0
            for (delta_x, delta_y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + delta_x, col + delta_y
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if grid[new_row][new_col] != height + 1:
                    continue
                
                res += dfs(grid, new_row, new_col, trailends)
            
            return res
        
        res = 0                 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    res += dfs(grid, row, col, set())
                    
        return res
                
    def solution2(self, filename):
        grid = self.readFile(filename)
        
        def dfs(grid, row, col):
            height = grid[row][col]
            if height == 9:
                return 1
            
            res = 0
            for (delta_x, delta_y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + delta_x, col + delta_y
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                if grid[new_row][new_col] != height + 1:
                    continue
                
                res += dfs(grid, new_row, new_col)
            
            return res
        
        res = 0                 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    res += dfs(grid, row, col)
                    
        return res
        
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day10/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day10/input.txt"))