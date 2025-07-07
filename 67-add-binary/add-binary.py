class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        remainder = 0
        output = []
        while i>=0 or j>=0:
            sum = 0
            if i>=0: 
                sum += int(a[i]) 
            if(j>=0):
                sum += int(b[j])
            sum += remainder
            output.insert(0,str(sum%2))
            remainder = sum//2
            j -= 1
            i -= 1
        if(remainder):
            output.insert(0,str(remainder))
        return "".join(output)
            
