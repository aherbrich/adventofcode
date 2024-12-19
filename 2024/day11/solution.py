class Solution:
    def readFile(self, filename):
        with open(filename) as file:
            for line in file:
                return list(map(int, line.strip().split()))
    
    def solution1(self, filename):
        nums = self.readFile(filename)
        
        def dfs(num, i):
            if i == 0:
                return 1
            
            
            if num == 0:
                return dfs(1, i-1)
            elif len(str(num)) % 2 == 0:
                left_num = int(str(num)[:len(str(num))//2])
                right_num = int(str(num)[len(str(num))//2:])
                return dfs(left_num, i-1) + dfs(right_num, i-1)
            else:
                return dfs(num*2024, i-1)
        
        res = 0
        for num in nums:
            res += dfs(num, 25)
        
        return res
            
    def solution2(self, filename):
        nums = self.readFile(filename)
        
        
        def dfs(num, i, cache):
            if i == 0:
                return 1
            
            if (num, i) in cache:
                return cache[(num, i)]
            
            if num == 0:
                cache[(num, i)] = dfs(1, i-1, cache)
            elif len(str(num)) % 2 == 0:
                left_num = int(str(num)[:len(str(num))//2])
                right_num = int(str(num)[len(str(num))//2:])
                cache[(num, i)] = dfs(left_num, i-1, cache) + dfs(right_num, i-1, cache)
            else:
                cache[(num, i)] = dfs(num*2024, i-1, cache)
            
            return cache[(num, i)] 
        
        res = 0
        for num in nums:
            res += dfs(num, 75, {})
        
        return res
            
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day11/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day11/input.txt"))