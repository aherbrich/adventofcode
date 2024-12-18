from copy import deepcopy

class Solution:
    def readFile(self, filename):
        grid = []
        with open(filename) as file:
            for line in file:
                chars = list(line.strip())
                grid.append(chars)
        
        return grid

    def findStart(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '^':
                    return i, j
        
    def nextStep(self, row, col, direction, grid):
        if direction == "up":
            if row == 0 or grid[row-1][col] != '#':
                return row - 1, col, direction
            return self.nextStep(row, col, "right", grid)
        elif direction == "right":
            if col == len(grid[row]) - 1 or grid[row][col+1] != '#':
                return row, col + 1, direction
            return self.nextStep(row, col, "down", grid)
        elif direction == "down":
            if row == len(grid) - 1 or grid[row+1][col] != '#':
                return row + 1, col, direction
            return self.nextStep(row, col, "left", grid)
        elif direction == "left":
            if col == 0 or grid[row][col-1] != '#':
                return row, col - 1, direction
            return self.nextStep(row, col, "up", grid)
    
    def outOfBounds(self, row, col, grid):
        return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])
    
    def leads_to_loop(self, row, col, direction, grid):
        tmp_grid = deepcopy(grid)
        
        def place_dir_marker(row, col, direction):
            if direction == "up":
                tmp_grid[row][col] = '^'
            elif direction == "right":
                tmp_grid[row][col] = '>'
            elif direction == "down":
                tmp_grid[row][col] = 'v'
            elif direction == "left":
                tmp_grid[row][col] = '<'
            
        while True:
            place_dir_marker(row, col, direction)
            
            row, col, direction = self.nextStep(row, col, direction, tmp_grid)
            if self.outOfBounds(row, col, tmp_grid):
                break
            
            if direction == "up" and tmp_grid[row][col] == '^':
                return True
            if direction == "right" and tmp_grid[row][col] == '>':
                return True
            if direction == "down" and tmp_grid[row][col] == 'v':
                return True
            if direction == "left" and tmp_grid[row][col] == '<':
                return True
            
        
    def solution1(self, filename):
        grid = self.readFile(filename)
        
        row, col = self.findStart(grid)
        
        res = 0
        direction = "up"
        while True:
            if grid[row][col] != 'X':
                res += 1
            grid[row][col] = 'X'
            
            row, col, direction = self.nextStep(row, col, direction, grid)
            if self.outOfBounds(row, col, grid):
                break
            
        return res
    
    def solution2(self, filename):
        # pretty inefficient solution, but it works
        grid = self.readFile(filename)
        
        row, col = self.findStart(grid)
        
        res = 0
        direction = "up"
        while True:
            # check if we can move in the current direction
            new_row, new_col, new_direction = self.nextStep(row, col, direction, grid)
            if self.outOfBounds(new_row, new_col, grid):
                break
            
            # if we have not checked if placing a wall at the new position 
            # leads to a loop, then do so
            if grid[new_row][new_col] != 'X':
                # place, check for loop and unplace a wall at the new position
                saved = grid[new_row][new_col]
                grid[new_row][new_col] = '#'
                if self.leads_to_loop(row, col, direction, grid):
                    res += 1
                grid[new_row][new_col] = saved
            
            # mark the new position as checked for loops
            grid[new_row][new_col] = 'X'
            
            # actually move to the new position
            row, col, direction = new_row, new_col, new_direction
            
        
        return res

    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day06/test.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day06/test.txt"))