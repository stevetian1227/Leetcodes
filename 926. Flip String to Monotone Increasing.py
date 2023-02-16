class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans=0
        count1=0
        for c in s:
            if c=='0':
                ans=min(ans+1,count1)
            else:
                count1+=1
        return ans