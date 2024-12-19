from collections import defaultdict

class Solution:
    def readFile(self, filename):
        num = ""
        
        with open(filename) as file:
            for line in file:
                num = line.strip()
            
        return num
    
    def expandDiskMap(self, diskMap):
        disk = []
        block = 0
        for i, digit in enumerate(diskMap):
            if i % 2 == 0:
                disk += [str(block)] * int(digit)
                block += 1
            else:
                disk += ["."] * int(digit)
        
        return disk
    
    def calculateChecksum(self, disk):
        res = 0
        for i in range(len(disk)):
            if disk[i] == ".":
                continue
            
            res += i * int(disk[i])

        return res
    
    def solution1(self, filename):
        diskmap = self.readFile(filename)
        
        disk = self.expandDiskMap(diskmap)
        
        l, r = 0, len(disk) - 1
        
        while l < r:
            if disk[l] != '.':
                l += 1
                continue
            
            if disk[r] == '.':
                r -= 1
                continue
            
            disk[l] = disk[r]
            disk[r] = '.'
            
            l += 1
            r -= 1
        
        return self.calculateChecksum(disk)
        
    def solution2(self, filename):
        # not efficient, but works
        
        diskmap = self.readFile(filename)
        
        disk = self.expandDiskMap(diskmap)
        
        r = len(disk) - 1
        
        while r > 0:
            # skip over empty space
            if disk[r] == '.':
                r -= 1
                continue
            
            # determine length of block
            block_len = 0
            block_id = disk[r]
            while r - block_len >= 0 and disk[r - block_len] == block_id:
                block_len += 1
            
            # find empty space to move block
            start = 0
            while start < r:                
                fits = True   
                for i in range(block_len):
                    if start + i >= r or disk[start + i] != ".":
                        start = start + i + 1
                        fits = False
                        break
                
                if fits:
                    # move block
                    for i in range(block_len):
                        disk[start + i] = block_id
                        disk[r - i] = '.'
                    break
                
            
            r -= block_len
        
        return self.calculateChecksum(disk)
    
print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day09/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day09/input.txt"))