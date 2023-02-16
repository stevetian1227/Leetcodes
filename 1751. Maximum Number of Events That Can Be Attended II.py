class Solution:
    def minimumLength(self, s: str) -> int:
        result = len(s)
        n = len(s)-1
        i = 0
        while (i<n)and(s[i]==s[n]):
            currentChar = s[i]
            while (i<len(s)) and (s[i] == currentChar):
                i+=1
            while (n>=0) and (s[n] == currentChar):
                n-=1
        if n<i:
            return 0
        else:
            return n-i+1