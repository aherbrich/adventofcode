from collections import defaultdict
from itertools import permutations

class Solution:
    def readFile(self, filename):
        nums = []
        with open(filename) as file:
            for line in file:
                nums.append(line.strip())
        
        return nums
    
    def isValidPath(self, path, start, forbidden):
        for step in path:
            if step == "^":
                start = (start[0] - 1, start[1])
            elif step == "v":
                start = (start[0] + 1, start[1])
            elif step == "<":
                start = (start[0], start[1] - 1)
            elif step == ">":
                start = (start[0], start[1] + 1)
            
            if start in forbidden:
                return False
        
        return True
        
    def calculateShortestPathsKeypad(self):
        grid = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '0': (3, 1),
            'A': (3, 2),
        }
        
        shortestPaths = defaultdict(set)
        
        for char1 in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'A']:
            for char2 in ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', 'A']:
                if char1 == char2:
                    shortestPaths[(char1, char2)].add("A")
                
                vertical_steps = ""
                if grid[char1][0] > grid[char2][0]:
                    vertical_steps = "^" * (grid[char1][0] - grid[char2][0])
                elif grid[char1][0] < grid[char2][0]:
                    vertical_steps = "v" * (grid[char2][0] - grid[char1][0])
                    
                horizontal_steps = ""
                if grid[char1][1] > grid[char2][1]:
                    horizontal_steps = "<" * (grid[char1][1] - grid[char2][1])
                elif grid[char1][1] < grid[char2][1]:
                    horizontal_steps = ">" * (grid[char2][1] - grid[char1][1])
                
                steps = vertical_steps + horizontal_steps
                
                perms = [''.join(p) for p in permutations(steps)]
                
                for p in perms:
                    # check if taking that route would lead to stepping over the gap at (3, 0)
                    if self.isValidPath(p, grid[char1], [(3, 0)]):
                        shortestPaths[(char1, char2)].add(p + "A")
                
                
                 
        return shortestPaths
    
    def calculateShortestPathsArrowpad(self):
        grid = {
            '^': (0, 1),
            'A': (0, 2),
            '<': (1, 0),
            'v': (1, 1),
            '>': (1, 2)
        }
        
        shortestPaths = defaultdict(set)
        
        for char1 in ['^', 'A', '<', 'v', '>']:
            for char2 in ['^', 'A', '<', 'v', '>']:
                if char1 == char2:
                    shortestPaths[(char1, char2)].add("A")
                
                vertical_steps = ""
                if grid[char1][0] > grid[char2][0]:
                    vertical_steps = "^" * (grid[char1][0] - grid[char2][0])
                elif grid[char1][0] < grid[char2][0]:
                    vertical_steps = "v" * (grid[char2][0] - grid[char1][0])
                    
                horizontal_steps = ""
                if grid[char1][1] > grid[char2][1]:
                    horizontal_steps = "<" * (grid[char1][1] - grid[char2][1])
                elif grid[char1][1] < grid[char2][1]:
                    horizontal_steps = ">" * (grid[char2][1] - grid[char1][1])
                
                steps = vertical_steps + horizontal_steps
                
                perms = [''.join(p) for p in permutations(steps)]
                
                for p in perms:
                    # check if taking that route would lead to stepping over the gap at (0, 0)
                    if self.isValidPath(p, grid[char1], [(0, 0)]):
                        shortestPaths[(char1, char2)].add(p + "A")
                        
        return shortestPaths
    
    def mergeShortestPaths(self, shortest_paths_keypad, shortest_paths_arrowpad):
        shortest_paths = defaultdict(list)
        
        for key in shortest_paths_keypad:
            shortest_paths[key] = list(shortest_paths_keypad[key])
        
        for key in shortest_paths_arrowpad:
            shortest_paths[key] = list(shortest_paths_arrowpad[key])
        
        return shortest_paths
    
    def solution(self, filename, max_depth):
        nums = self.readFile(filename)
        
        shortest_paths_keypad = self.calculateShortestPathsKeypad()
        shortest_paths_arrowpad = self.calculateShortestPathsArrowpad()
        
        shortest_paths = self.mergeShortestPaths(shortest_paths_keypad, shortest_paths_arrowpad)
        
        def dfs(depth, src, dst, cache):
            if depth == max_depth:
                return len(shortest_paths[(src, dst)][0])
            
            if (depth, src, dst) in cache:
                return cache[(depth, src, dst)]
            
            paths = shortest_paths[(src, dst)]
            path_lens = [0 for _ in range(len(paths))]
            
            for i, path in enumerate(paths):
                prev = 'A'
                for next_dst in path:
                    path_lens[i] += dfs(depth+1, prev, next_dst, cache)
                    prev = next_dst
            
            cache[(depth, src, dst)] = min(path_lens)
            
            return cache[(depth, src, dst)]
        
        
        res = 0
        for num in nums:
            # calculate the length of the expanded string
            expanded_len = 0
            prev_c = 'A'
            for c in num:
                expanded_len += dfs(0, prev_c, c, {})
                prev_c = c

            # calculate the AoC score
            n = int("".join(list(filter(lambda x: x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], num))))
            res += expanded_len * n
        
        return res
            
       
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day21/input.txt", 2))
print(Solution().solution("/Users/aherbrich/src/myprojects/adventofcode24/2024/day21/input.txt", 25))