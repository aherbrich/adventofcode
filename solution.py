class Solution:    
    def findDistances(self, filename):
        left = []
        right = []
        
        with open(filename) as file:
            for line in file:
                l, r = list(map(int, line.strip().split()))
                left.append(l)
                right.append(r)
        
        left.sort()
        right.sort()
        
        res = 0
        
        for l, r in zip(left, right):
            res += abs(l - r)
        
        
        return res
    
    def findSimilarity(self, filename):
        left = []
        right = []
        
        with open(filename) as file:
            for line in file:
                l, r = list(map(int, line.strip().split()))
                left.append(l)
                right.append(r)
                
        counts = {}
        
        for val in right:
            if val not in counts:
                counts[val] = 1
            else:
                counts[val] += 1
        
        res = 0
        
        for val in left:
            count = counts[val] if val in counts else 0
            res += val * count
            
        return res
                
            

        