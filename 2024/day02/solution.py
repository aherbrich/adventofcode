class Solution:    
    def isSafe(self, nums):
        diffs = [nums[i] - nums[i+1] for i in range(len(nums)-1)]
        
        if any([diff == 0 for diff in diffs]):
            return False
        
        if any([abs(diff) > 3 for diff in diffs]):
            return False
        
        is_increasing = any([diff > 0 for diff in diffs])
        is_decreasing = any([diff < 0 for diff in diffs])
        
        if is_increasing and is_decreasing:
            return False
        
        return True
            
    def findSafe(self, filename):
        safe = 0
        with open(filename) as file:
            for line in file:
                nums = list(map(int, line.strip().split()))
                if self.isSafe(nums):
                    safe += 1
                    
        return safe
    
    def findSafeWithException(self, filename):
        safe = 0
        with open(filename) as file:
            for line in file:
                nums = list(map(int, line.strip().split()))
                if self.isSafe(nums):
                    safe += 1
                else:
                    for i in range(len(nums)):
                        if self.isSafe(nums[:i] + nums[i+1:]):
                            safe += 1
                            break
                    
        return safe