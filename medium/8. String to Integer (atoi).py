from typing import List
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # 去掉左侧空格
        if not s:  # 如果字符串为空
            return 0
        
        # 确定符号
        flag = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:  # 如果有符号，跳过它
            s = s[1:]
        
        # 提取数字部分
        num = ""
        for c in s:
            if c.isdigit():
                num += c
            else:
                break
        
        if not num:  # 如果没有数字
            return 0
        
        # 转换为整数并加符号
        result = int(num) * flag
        
        # 限制范围在 [-2^31, 2^31-1]
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        return max(INT_MIN, min(INT_MAX, result))