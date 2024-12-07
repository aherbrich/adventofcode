class Solution: 
    def solve(self, filename):
        forbidden = set() # if (x,y) in forbidden, than x is not allowed before y
        
        res = 0
        with open(filename) as file:
            parsing_rules = True
            for line in file:
                # 1. Parse the rules
                if line.strip() == "":
                    parsing_rules = False
                    continue
                
                if parsing_rules:
                    x, y = list(map(int, line.strip().split("|")))
                    forbidden.add((y, x))
                else:
                    # 2. Actual update rule checker logic
                    nums = list(map(int, line.strip().split(",")))
                    skip = False
                    for i in range(len(nums)-1):
                        if (nums[i], nums[i+1]) in forbidden:
                            skip = True
                            break
                    
                    if skip:
                        continue
                    
                    res += nums[int(len(nums)/2)]
                    
        return res
       
    def solve2(self, filename):
        forbidden = set() # if (x,y) in forbidden, than x is not allowed before y
        
        res = 0
        with open(filename) as file:
            parsing_rules = True
            for line in file:
                # 1. Parse the rules
                if line.strip() == "":
                    parsing_rules = False
                    continue
                
                if parsing_rules:
                    x, y = list(map(int, line.strip().split("|")))
                    forbidden.add((y, x))
                else:
                    # 2. Actual update rule checker logic
                    nums = list(map(int, line.strip().split(",")))
                    skip = False
                    for i in range(len(nums)-1):
                        if (nums[i], nums[i+1]) in forbidden:
                            skip = True
                            break
                    
                    if skip:
                        # O(n^2) for sorting, but who cares
                        for _ in range(len(nums)):
                            for i in range(len(nums)-1):
                                if (nums[i], nums[i+1]) in forbidden:
                                    nums[i], nums[i+1] = nums[i+1], nums[i]
                        
                    
                        res += nums[int(len(nums)/2)]
                    
        return res

        