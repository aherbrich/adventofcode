class Solution:
    def readFile(self, filename):
        grid = []
        with open(filename) as file:
            for line in file:
                grid.append(list(line.strip()))
        return grid
    
    def findStart(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "S":
                    return (row, col)
                
    def printMap(self, grid):
        for row in grid:
            for col in row:
                print(str(col).rjust(3), end='')
            print()
        print()
    
    def getPathLength(self, grid):
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "." or grid[row][col] == "E":
                    res += 1
        return res
    
    def getHelperMaps(self, grid, start_row, start_col):
        until_end_map = [row[:] for row in grid]
        upto_here_map = [row[:] for row in grid]
        path = set()
        
        path_len = self.getPathLength(grid)
        stack = [(start_row, start_col, 0)]
        while stack:
            row, col, time = stack.pop()
            until_end_map[row][col] = path_len - time
            upto_here_map[row][col] = time
            path.add((row, col))
            
            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + delta_row, col + delta_col
                
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                
                if until_end_map[new_row][new_col] == "." or until_end_map[new_row][new_col] == "E":
                    stack.append((new_row, new_col, time + 1))
                    break
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "#":
                    until_end_map[row][col] = '-'
                    upto_here_map[row][col] = '-'
                    
        return until_end_map, upto_here_map, path
                 
    def solution(self, filename, max_distance):
        grid = self.readFile(filename)
        
        row, col = self.findStart(grid)
        
        time_without_cheat = self.getPathLength(grid)
        until_end, upto_here, path = self.getHelperMaps(grid, row, col)
        
        
        res = 0
        for row_1, col_1 in path:
            for row_2, col_2 in path:        
                if upto_here[row_1][col_1] > upto_here[row_2][col_2]:
                    continue
                
                distance = abs(row_1 - row_2) + abs(col_1 - col_2)
                if distance <= max_distance:
                    upto_cheat = upto_here[row_1][col_1]
                    from_cheat = until_end[row_2][col_2]
                    time_with_cheat = upto_cheat + from_cheat + distance
                    saved_time = time_without_cheat - time_with_cheat
                    if saved_time >= 100:
                        res += 1
                        
        return res
         
    
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day20/input.txt", 2))
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day20/input.txt", 20))