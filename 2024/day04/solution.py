class Solution:
    def findXMAS(self, filename):
        grid = []
        with open(filename) as file:
            for line in file:
                chars = list(line.strip())
                grid.append(chars)
        
        res = 0
        for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            for row in range(max(-3*i, 0), len(grid) + min(0, -3*i)):
                for col in range(max(-3*j, 0), len(grid[row]) + min(0, -3*j)):
                    if grid[row][col] == 'X':
                        chars = [grid[row+k*i][col+k*j] for k in range(1,4)]
                        if "".join(chars) == "MAS":
                            res += 1
                            
        return res
                            
    def findMAS(self, filename):              
        grid = []
        with open(filename) as file:
            for line in file:
                chars = list(line.strip())
                grid.append(chars)
        
        res = 0
        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[row]) - 1):
                if grid[row][col] == 'A':
                    if grid[row-1][col-1] == 'M' and grid[row-1][col+1] == 'M':
                        if grid[row+1][col-1] == 'S' and grid[row+1][col+1] == 'S':
                            res += 1
                    elif grid[row+1][col-1] == 'M' and grid[row+1][col+1] == 'M':
                        if grid[row-1][col-1] == 'S' and grid[row-1][col+1] == 'S':
                            res += 1
                    elif grid[row-1][col+1] == 'M' and grid[row+1][col+1] == 'M':
                        if grid[row-1][col-1] == 'S' and grid[row+1][col-1] == 'S':
                            res += 1
                    elif grid[row-1][col-1] == 'M' and grid[row+1][col-1] == 'M':
                        if grid[row-1][col+1] == 'S' and grid[row+1][col+1] == 'S':
                            res += 1
        
        print(res)
        return res
                
                
                    

Solution().findXMAS("/Users/aherbrich/src/myprojects/adventofcode24/2024/day04/test.txt")