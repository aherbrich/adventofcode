import re

class Solution:
    def findMultiplications(self, filename):
        res = 0
        with open(filename) as file:
            for line in file:    
                matches = re.findall(r"mul\(([1-9][0-9]*),([1-9][0-9]*)\)", line)
                for num1, num2 in matches:
                    res += int(num1) * int(num2)
                    
        return res

    def findMultiplicationsWithEnable(self, filename):
        res = 0
        enabled = True
        with open(filename) as file:
            for line in file:    
                matches = re.findall(r"mul\(([1-9][0-9]*),([1-9][0-9]*)\)|(do\(\))|(don't\(\))", line)
                for num1, num2, do, dont in matches:
                    if do:
                        enabled = True
                    elif dont:
                        enabled = False
                    else:
                        if enabled:
                            res += int(num1) * int(num2)
                    
        return res