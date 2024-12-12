from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        ans = []
        if n > m:
            return ans
        def hash_(s):
            cs = [0] * 26
            for c in s:
                cs[ord(c) - ord('a')] += 1
            return cs

        p_hash = hash_(p)
        cur_hash = hash_(s[:n])
        if p_hash == cur_hash:
            ans.append(0)
        for i in range(1, m - n + 1):
            cur_hash[ord(s[i-1]) - ord('a')] -= 1
            cur_hash[ord(s[i+n-1]) - ord('a')] += 1
            if p_hash == cur_hash:
                ans.append(i)
        return ans