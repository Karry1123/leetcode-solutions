from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:  # 特殊情况处理
            return 0
        
        def binarysearch(left, right):
            if left > right:  # 递归结束条件
                return right  # 返回不超过平方根的整数部分
            
            mid = (left + right) // 2
            if mid * mid == x:  # 找到精确平方根
                return mid
            elif mid * mid < x:  # 搜索右区间
                return binarysearch(mid + 1, right)
            else:  # 搜索左区间
                return binarysearch(left, mid - 1)
        
        return binarysearch(0, x)