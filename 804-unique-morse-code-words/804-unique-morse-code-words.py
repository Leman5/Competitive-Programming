class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for i in words:
            encoded = ""
            for j in i:
                encoded += mos[ord(j)-97]
            s.add(encoded)
        return len(s)