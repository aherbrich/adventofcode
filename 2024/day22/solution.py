class Solution:
    def readFile(self, filename):
        nums = []
        for line in open(filename):
            nums.append(int(line.strip()))
        
        return nums
            
    def evolveSecretNum(self, num):
        num = num ^ (num * 64)
        num = num % 16777216
        
        num = num ^ (int(num/32))
        num = num % 16777216
        
        num = num ^ (num * 2048)
        num = num % 16777216
        
        return num

    def solution1(self, filename):
        nums = self.readFile(filename)
        
        res = 0
        for num in nums:
            for _ in range(2000):
                num = self.evolveSecretNum(num)
            res += num
    
        return res
                
            
    def solution2(self, filename):
        # super slow, but works (solved with equivalent code in julia)
        nums = self.readFile(filename)
        
        bananas = [[] for _ in range(len(nums))]
        deltas = [[] for _ in range(len(nums))]
        for i, num in enumerate(nums):
            last_digit = num % 10
            for _ in range(2000):
                num = self.evolveSecretNum(num)
                bananas[i].append(num % 10)
                deltas[i].append((num % 10) - last_digit)
                last_digit = num % 10
        
        maxi = 0
        best_seq = []

        for a in range(-9, 10):
            for b in range(-9, 10):
                for c in range(-9, 10):
                    for d in range(-9, 10):
                        seq = (a, b, c, d)
                        
                        res = 0
                        for k in range(len(nums)):
                            for i in range(len(bananas[k]) - 3):
                                match = True
                                for j in range(4):
                                    if deltas[k][i + j] != seq[j]:
                                        match = False
                                        break
                                
                                if match:
                                    res += bananas[k][i + 3]
                                    break

                        if res > maxi:
                            best_seq = seq
                        maxi = max(maxi, res)

                        # print(f"({a}, {b}, {c}, {d}) = {maxi} seq = {best_seq}")

        return maxi, best_seq

print(Solution().solution1("/Users/aherbrich/src/myprojects/adventofcode24/2024/day22/input.txt"))
print(Solution().solution2("/Users/aherbrich/src/myprojects/adventofcode24/2024/day22/input.txt"))