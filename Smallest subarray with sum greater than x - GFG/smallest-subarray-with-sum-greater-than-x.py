class Solution:
    def smallestSubWithSum(self, arr, n, x):
        # Initializing variables
        min_len = n + 1
        start = 0
        end = 0
        curr_sum = 0
    
        # Traversing through the array
        while (end < n):
            # Adding the current element to the sum
            curr_sum += arr[end]
    
            # If sum is greater than x, remove elements from the start
            while (curr_sum > x and start <= end):
                # Updating the minimum length
                min_len = min(min_len, end - start + 1)
                curr_sum -= arr[start]
                start += 1
    
            end += 1
    
        # If no subarray found
        if min_len == n + 1:
            return -1
        else:
            return min_len
        # Your code goes here 
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends