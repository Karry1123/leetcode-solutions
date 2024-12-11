from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic=Counter(t)
        count=len(t)
        start=0
        res=""
        for end,c in enumerate(s):
            if dic[c]>0:
                count-=1
            dic[c]-=1
            if count==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[start] 
                    if dic[c]==0:
                        break
                    dic[c]+=1
                    start+=1
                if res=="":   #记录结果
                    res=s[start:end+1]
                else:
                    if len(res)>end-start+1:
                        res=s[start:end+1]
                dic[s[start]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                count=1
                start+=1
        return res