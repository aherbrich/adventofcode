class Solution:
    def predictPath(self, filename):
        grid = []
        with open(filename) as file:
            for line in file:
                chars = list(line.strip())
                grid.append(chars)
        
        # 1. find initial position
        row, col = 0, 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '^':
                    grid[i][j] = '.'
                    row, col = i, j
                    break
                
        # 2. run through maze until exit and count new fields encountered
        res = 0
        direc = [(-1, 0), (0, 1), (1,0), (0, -1)]
        dir_idx = 0
        while True:
            if grid[row][col] == '.':
                res += 1
                grid[row][col] = 'X'
            
            x, y = direc[dir_idx]
            new_row, new_col = row + x, col + y
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[col]):
                break
            
            if grid[new_row][new_col] == '#':
                dir_idx = (dir_idx + 1) % 4
                continue
            
            row, col = new_row, new_col
            
        return res
    
print(Solution().predictPath("/Users/aherbrich/src/myprojects/adventofcode24/2024/day06/test.txt"))