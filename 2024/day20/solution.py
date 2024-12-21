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
        distance_grid = [row[:] for row in grid]
        path_grid = [row[:] for row in grid]
        path = set()
        
        path_len = self.getPathLength(grid)
        stack = [(start_row, start_col, 0)]
        while stack:
            row, col, time = stack.pop()
            distance_grid[row][col] = path_len - time
            path_grid[row][col] = time
            path.add((row, col))
            
            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + delta_row, col + delta_col
                
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                    continue
                
                if distance_grid[new_row][new_col] == "." or distance_grid[new_row][new_col] == "E":
                    stack.append((new_row, new_col, time + 1))
                    break
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "#":
                    distance_grid[row][col] = '-'
                    path_grid[row][col] = '-'
                    
        return distance_grid, path_grid, path
    
    def calculateSavedTime(self, grid, path, start_row, start_col, cheats_allowed):
        tmp_grid = [row[:] for row in grid]
        saved_times = {}
        saved_routes = {}
        
        stack = [(start_row, start_col, 1, cheats_allowed, set(), (-1, -1), (-1, -1))]
        path_len = len(path)
        while stack:
            row, col, time, cheats_left, seen, begin, end = stack.pop()
            
            if grid[row][col] == "E":
                saved = path_len - time
                if saved > 0:
                    if saved not in saved_routes:
                        saved_routes[saved] = set()
                    if (begin, end) not in saved_routes[saved]:
                        saved_times[saved] = saved_times.get(saved, 0) + 1
                    saved_routes[saved].add((begin, end))
                continue
            elif cheats_left < cheats_allowed and (row, col) in path:
                saved = path[(row, col)] + 1 - time
                if saved > 0:
                    if saved not in saved_routes:
                        saved_routes[saved] = set()
                    if (begin, end) not in saved_routes[saved]:
                        saved_times[saved] = saved_times.get(saved, 0) + 1
                    saved_routes[saved].add((begin, end))
                continue
            
            if (row, col) not in path and cheats_left == 0:
                continue
            
            seen_cpy = seen.copy()
            seen_cpy.add((row, col))
            
            for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    
                new_row, new_col = row + delta_row, col + delta_col
                
                if new_row < 0 or new_row >= len(tmp_grid) or new_col < 0 or new_col >= len(tmp_grid[0]) or (new_row, new_col) in seen:
                    continue
                
                # 1. just go normal, no cheating
                if tmp_grid[new_row][new_col] == "." or tmp_grid[new_row][new_col] == "E":
                    cheats_left_cpy = cheats_left - 1 if grid[row][col] == "#" else cheats_left
                    end_cpy = (new_row, new_col) if grid[row][col] == "#" else end
                    stack.append((new_row, new_col, time + 1, cheats_left_cpy, seen_cpy, begin, end_cpy))
                # # 2. cheating
                if tmp_grid[new_row][new_col] == "#":
                    if cheats_left > 0:
                        begin_cpy = (row, col) if cheats_left == cheats_allowed else begin
                        stack.append((new_row, new_col, time + 1, cheats_left - 1, seen_cpy, begin_cpy, end))
            
            
        
        return saved_times
                
                
    def solution(self, filename, max_distance):
        grid = self.readFile(filename)
        
        row, col = self.findStart(grid)
        
        time_without_cheat = self.getPathLength(grid)
        distance_map, path_map, path = self.getHelperMaps(grid, row, col)
        
        
        saved_times = {}
        for field_1 in path:
            for field_2 in path:
                if path_map[field_1[0]][field_1[1]] > path_map[field_2[0]][field_2[1]]:
                    continue
                
                distance = abs(field_1[0] - field_2[0]) + abs(field_1[1] - field_2[1])
                if distance <= max_distance:
                    upto_cheat = path_map[field_1[0]][field_1[1]]
                    from_cheat = distance_map[field_2[0]][field_2[1]]
                    time_with_cheat = upto_cheat + from_cheat + distance
                    saved_time = time_without_cheat - time_with_cheat
                    if saved_time > 0:
                        saved_times[saved_time] = saved_times.get(saved_time, 0) + 1
        
        res = 0           
        for k in sorted(saved_times.keys(), reverse=True):
            if k >= 100:
                res += saved_times[k]
        
        return res
         
    
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day20/input.txt", 2))
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day20/input.txt", 20))