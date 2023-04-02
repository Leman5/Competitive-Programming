class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        open = close = n
        temp = ""
        def generate(open,close,temp):
            if(open==0 and close == 0):
                output.append(temp)
            if(open>0):
                generate(open-1,close,temp+"(")
            if(close>open):
                generate(open,close-1,temp+")")
            return 
        generate(open,close,temp)
        return output
            