from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        if matrix[m-1][n-1]<target or matrix[0][0]>target:
            return False
        up=0
        down=m-1
        mid=(up+down)//2
        while up<=down:
            mid=(up+down)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]>target:
                down=mid-1
            else:
                if matrix[mid][n-1]==target:
                    return True
                elif matrix[mid][n-1]>target:
                    break
                else:
                    up=mid+1
        left=0
        right=n-1
        while left<=right:
            cent=(left+right)//2
            if matrix[mid][cent]==target:
                return True
            elif matrix[mid][cent]<target:
                left=cent+1
            else:
                right=cent-1
        return False