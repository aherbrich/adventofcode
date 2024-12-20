class Solution:
    def readFile(self, filename):
        grid = []
        with open(filename) as file:
            for line in file:
                grid.append(list(line.strip()))
        return grid
    
    def dfs(self, grid, row, col, region):
            region.add((row, col))
            
            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + delta_row, col + delta_col
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                
                if grid[row][col] == grid[new_row][new_col] and (new_row, new_col) not in region:
                    self.dfs(grid, new_row, new_col, region)
    
    def remove_region(self, grid, region):
        for row, col in region:
            grid[row][col] = "-"
                
    def solution1(self, filename):
        grid = self.readFile(filename)
        
        def count_perimeter(region):
            res = 0
            for row, col in region:
                no_neighbor_sides = 0
                for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_row, new_col = row + delta_row, col + delta_col
                    if (new_row, new_col) not in region:
                        no_neighbor_sides += 1
                res += no_neighbor_sides
            return res
                        
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != "-":
                    region = set()
                    self.dfs(grid, row, col, region)
                    res += len(region) * count_perimeter(region)
                    self.remove_region(grid, region)
                    
        return res
                    
                
            
    def solution2(self, filename):
        grid = self.readFile(filename)
        
        def nr_of_consecutive(lst):
            if not lst:
                return 0
            
            lst.sort()
            res = 1
            
            for i in range(1, len(lst)):
                if lst[i] - lst[i-1] > 1:
                    res += 1
                    
            return res
        
        def count_vertical_sides(region):
            region_lst = list(region)
            # sort by column (and then row)
            region_lst.sort(key=lambda x: (x[1], x[0]))
            
            res = 0
            
            cur_col = region_lst[0][1]
            left_lst = []
            right_lst = []
            i = 0
            while i < len(region_lst):
                row, col = region_lst[i][0], region_lst[i][1]
                
                if col != cur_col:
                    cur_col = col
                    res += nr_of_consecutive(left_lst) + nr_of_consecutive(right_lst)
                    left_lst, right_lst = [], []
                    continue
                
                if (row, col + 1) not in region:
                    right_lst.append(row)
                    
                if (row, col - 1) not in region:
                    left_lst.append(row)
                    
                i += 1
            
            res += nr_of_consecutive(left_lst) + nr_of_consecutive(right_lst)
            
            return res
        
        def count_horizontal_sides(region):
            region_lst = list(region)
            # sort by row (and then column)
            region_lst.sort()
            
            res = 0
            
            cur_row = region_lst[0][0]
            top_lst = []
            bottom_lst = []
            i = 0
            while i < len(region_lst):
                row, col = region_lst[i][0], region_lst[i][1]
                
                if row != cur_row:
                    cur_row = row
                    res += nr_of_consecutive(top_lst) + nr_of_consecutive(bottom_lst)
                    top_lst, bottom_lst = [], []
                    continue
                
                if (row + 1, col) not in region:
                    bottom_lst.append(col)
                    
                if (row - 1, col) not in region:
                    top_lst.append(col)
                    
                i += 1
            
            res += nr_of_consecutive(top_lst) + nr_of_consecutive(bottom_lst)
            
            return res
            
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != "-":
                    region = set()
                    self.dfs(grid, row, col, region)
                    res += len(region) * (count_horizontal_sides(region) + count_vertical_sides(region))
                    self.remove_region(grid, region)
                    
        return res
                    
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day12/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day12/input.txt"))