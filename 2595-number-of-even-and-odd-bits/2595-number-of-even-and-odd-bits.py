class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        binary = ''
        while(n>0):
            binary += str(n%2)
            n = n//2
        # binary = binary[::-1]
        even , odd = 0 , 0
        for i in range(len(binary)):
            if(binary[i]==str(1)):
                if(i%2 == 0):
                    even += 1
                else:
                    odd += 1
        return [even,odd]