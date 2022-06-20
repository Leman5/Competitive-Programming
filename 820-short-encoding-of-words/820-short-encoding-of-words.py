class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len,reverse=True)
        out = ""
        for i in words:
            if(out.find(i+"#")== -1):
                out += i+"#"
                # print(out)
        return len(out)