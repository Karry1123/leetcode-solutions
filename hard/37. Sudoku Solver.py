from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        stack = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        row = [[] for _ in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!=".":
                    num=int(board[i][j])
                    stack[i//3*3+j//3].append(num)
                    column[j].append(num)
                    row[i].append(num)
        
        def backtrack(i,j):
            if i==9:
                return True
            next_i = i if j < 8 else i + 1
            next_j = j + 1 if j < 8 else 0
            if board[i][j]!=".":
                return backtrack(next_i,next_j)
            for a in range(1,10):
                if a not in row[i] and a not in column[j] and a not in stack[i//3*3+j//3]:
                    board[i][j]=str(a)
                    row[i].append(a)
                    column[j].append(a)
                    stack[i//3*3+j//3].append(a)
                    if backtrack(next_i, next_j):
                        return True

                    board[i][j]="."
                    row[i].remove(a)
                    column[j].remove(a)
                    stack[i//3*3+j//3].remove(a)
            return False
        backtrack(0,0)