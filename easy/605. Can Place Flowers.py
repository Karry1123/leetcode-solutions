from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        count=0
        for i in range(len(flowerbed)-2,0,-1):
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                flowerbed[i]=1
                count+=1
        if flowerbed[0]==0 and flowerbed[1]==0:
            count+=1
        return count>=n