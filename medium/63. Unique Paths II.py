from collections import deque
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n,m=len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        for row in range(n):
            for column in range(m):
                # 第一格初始化为1
                if row==0 and column==0:
                    obstacleGrid[row][column]=1

                #遇到石头将格子设为0    
                elif obstacleGrid[row][column]==1:
                    obstacleGrid[row][column]=0

                #无石头的情况
                else:
                    #第一行
                    if row==0:
                        obstacleGrid[row][column]=obstacleGrid[row][column-1]
                    #第一列
                    elif column==0:
                        obstacleGrid[row][column]=obstacleGrid[row-1][column]
                    else:
                        obstacleGrid[row][column]=obstacleGrid[row-1][column]+obstacleGrid[row][column-1]
        
        return obstacleGrid[n-1][m-1]