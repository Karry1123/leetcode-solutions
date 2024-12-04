from typing import List
from typing import Optional
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 用于存储每行、每列、每个 3x3 宫的数据
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":  # 跳过空格
                    continue

                # 确定当前数字属于哪个 3x3 宫
                box_index = (i // 3) * 3 + (j // 3)

                # 检查数字是否已经存在于对应的行、列或 3x3 宫
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False

                # 将数字添加到对应的集合中
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True