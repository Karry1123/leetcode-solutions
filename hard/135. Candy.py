from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=len(ratings)
        if l==1:
            return 1
        cur=0
        cnt=0
        stack=[1]*l
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                stack[i]=stack[i-1]+1
                cur=i
            elif ratings[i]==ratings[i-1]:
                cur=i
            else:
                if stack[i]==stack[i-1] and stack[cur]-stack[i]>=i-cur:
                    cnt+=i-cur-1
                elif stack[i]==stack[i-1]:
                    cnt+=i-cur
        cnt+=sum(stack)
        return cnt