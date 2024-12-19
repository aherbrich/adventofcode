from collections import defaultdict

class Solution:
    def readFile(self, filename):
        grid = []
        
        with open(filename) as file:
            for line in file:
                grid.append(list(line.strip()))
            
        return grid
    
    def extractChars(self, grid):
        chars = defaultdict(list)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != ".":
                    chars[grid[row][col]].append((row, col))
        
        return chars
    
    def inBounds(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def solution1(self, filename):
        grid = self.readFile(filename)
        chars = self.extractChars(grid)
        
        antennas = set()
        for _, coords in chars.items():
            for i in range(len(coords)):
                for j in range(len(coords)):
                    if i == j:
                        continue
                    
                    delta_x = coords[i][0] - coords[j][0]
                    delta_y = coords[i][1] - coords[j][1]
                
                    if self.inBounds(grid, coords[i][0] + delta_x, coords[i][1] + delta_y):
                        antennas.add((coords[i][0] + delta_x, coords[i][1] + delta_y))
        
        return len(antennas)
    
    def solution2(self, filename):
        grid = self.readFile(filename)
        chars = self.extractChars(grid)
        
        antennas = set()
        for _, coords in chars.items():
            for i in range(len(coords)):
                for j in range(len(coords)):
                    if i == j:
                        continue
                    
                    delta_x = coords[i][0] - coords[j][0]
                    delta_y = coords[i][1] - coords[j][1]
                    
                    k = 0
                    while self.inBounds(grid, coords[i][0] + k*delta_x, coords[i][1] + k*delta_y):
                        antennas.add((coords[i][0] + k*delta_x, coords[i][1] + k*delta_y))
                        k += 1
        
        return len(antennas)
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day08/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day08/input.txt"))