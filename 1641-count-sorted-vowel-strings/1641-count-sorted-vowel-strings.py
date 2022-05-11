class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [[],[1,1,1,1,1]]
        prev_sum = sum(arr[-1])
        for i in range(2,n+1):
            arr.append([0]*5)
            for j in range(5):
                arr[i][j] = prev_sum
                prev_sum -= arr[i-1][j]
            prev_sum = sum(arr[-1])
        return sum(arr[-1])
        