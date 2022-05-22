def isPalindrome(s):
    return s == s[::-1]

class Solution(object):
    def countSubstrings(self, s):
        ranges = dict()
        for i, c in enumerate(s):
            if c in ranges:
                ranges[c].append(i)
            else:
                ranges[c] = [i]
        count = 0
        for rangeSet in ranges.values():
            for leftIndex, leftValue in enumerate(rangeSet):
                for rightValue in rangeSet[leftIndex:]:
                    if isPalindrome(s[leftValue:rightValue+1]):
                        count += 1
        return count