class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bitCount = 0
        while n:
            
            n -= 2**int(log(n, 2))
            bitCount += 1
                  
        return bitCount