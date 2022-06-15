class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp={}
        #sort words based on their len
        #here instead of adding letter to the words and finding the longest chain,
        #we remove one character at a time and check if we previouly visited that character , 
        #and if we visited it then curr words chain length is max(currwordChainLength,prevWordChainLength+1)
        
        #then we just have to return maximum chain length
        
        maxChainLength=1
        for word in sorted(words,key=len):
            dp[word]=1
            
            for i in range(len(word)):
                prevWord=word[:i]+word[i+1:]
                if prevWord in dp:
                    dp[word]=max(dp[word],dp[prevWord]+1)
                    maxChainLength=max(maxChainLength,dp[word])
                
        
        return maxChainLength