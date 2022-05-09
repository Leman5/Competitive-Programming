class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
#         table = [[],['a', 'b', 'c'],
#             ['d', 'e', 'f'],
#             ['g', 'h', 'i'],
#             ['j', 'k', 'l'],
#             ['m', 'n', 'o'],
#             ['p', 'q', 'r','s'],
#             ['t', 'u','v'],
#             [ 'w', 'x','y', 'z']]
#         pressedKeys = [int(x) for x in digits]
#         def findCombinations(input: list, table: list) -> list:
#             # vector of strings to store output
#             out, temp = [], []

#             # stores index of first occurrence
#             # of the digits in input
#             mp = dict()

#             # maintains index of current digit considered
#             index = 0

#             # for each digit
#             for d in input:

#                 # store index of first occurrence
#                 # of the digit in the map
#                 if d not in mp:
#                     mp[d] = index

#                 # clear vector contents for future use
#                 temp.clear()
#                 for i in range(len(table[d - 1])):

#                     # for first digit, simply push all its
#                     # mapped characters in the output list
#                     if index == 0:
#                         s = table[d - 1][i]
#                         out.append(s)

#                     # from second digit onwards
#                     if index > 0:

#                         # for each string in output list
#                         # append current character to it.
#                         for string in out:

#                             # convert current character to string
#                             s = table[d - 1][i]

#                             # Imp - If this is not the first occurrence
#                             # of the digit, use same character as used
#                             # in its first occurrence
#                             if mp[d] != index:
#                                 s = string[mp[d]]

#                             string = string + s

#                             # store strings formed by current digit
#                             temp.append(string)

#                         # nothing more needed to be done if this
#                         # is not the first occurrence of the digit
#                         if mp[d] != index:
#                             break

#                 # replace contents of output list with temp list
#                 if index > 0:
#                     out = temp.copy()
#                 index += 1
#             return out
#         out  = (findCombinations(pressedKeys,table))
#         return out
        
        number_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def dfs(digits):
            arr=[]
            if not digits:
                return ['']
            for char in number_dict[digits[0]]:
                for i in dfs(digits[1::]):
                    arr.append(char+i)
            return arr
			
        if not digits:
            return []
        return dfs(digits)