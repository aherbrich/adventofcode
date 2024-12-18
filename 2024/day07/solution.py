import math

class Solution:
    def readFile(self, filename):
        targets = []
        nums = []
        
        with open(filename) as file:
            for line in file:
                parts = line.strip().split()
                parts[0] = parts[0][:-1] # remove the ":" from the target
                parts = list(map(int, parts))
                
                targets.append(parts[0])
                nums.append([parts[i] for i in range(1, len(parts))])
        
        return targets, nums
    

    
    def solution1(self, filename):
        targets, nums = self.readFile(filename)
        
        def isValid(target, nums, i, cache):
            if i == 0:
                return nums[i] == target
            
            if (target, i) in cache:
                return cache[(target, i)]
            
            byAddition = isValid(target-nums[i], nums, i-1, cache)
            byMultiplication = target % nums[i] == 0 and isValid(target//nums[i], nums, i-1, cache)
            
            cache[(target, i)] = byAddition or byMultiplication
        
            return cache[(target, i)]
        
        res = 0
        for i in range(len(targets)):
            if isValid(targets[i], nums[i], len(nums[i])-1, {}):
                res += targets[i]
        
        return res
    
    def solution2(self, filename):
        targets, nums = self.readFile(filename)
        
        def isValid(target, nums, i, cache):
            if i == 0:
                return nums[i] == target
            
            if (target, i) in cache:
                return cache[(target, i)]
            
            byAddition = isValid(target-nums[i], nums, i-1, cache)
            byMultiplication = target % nums[i] == 0 and isValid(target//nums[i], nums, i-1, cache)
            
            shift = 10**int(math.ceil(math.log10(nums[i] + 1))) # number of digits in nums[i]
            byConcatenation = (target - nums[i]) % shift == 0 and isValid((target - nums[i]) // shift, nums, i-1, cache)

            cache[(target, i)] = byAddition or byMultiplication or byConcatenation
            
            return cache[(target, i)]
        
        res = 0
        for i in range(len(targets)):
            if isValid(targets[i], nums[i], len(nums[i])-1, {}):
                res += targets[i]
        
        return res
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day07/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day07/input.txt"))