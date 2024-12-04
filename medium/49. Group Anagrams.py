from typing import List
from typing import Optional
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}  # 用于存储分组信息
        for word in strs:
            # 将 Counter 转换为不可变的元组作为键
            key = tuple(sorted(word))  
            if key in dic:
                dic[key].append(word)  # 如果键已存在，追加当前单词
            else:
                dic[key] = [word]  # 如果键不存在，初始化分组

        return list(dic.values())  # 返回所有分组