class Solution:
    def isValidSudoku(self, n: List[List[str]]) -> bool:
        for i in range(0,9):
            seen1=set()
            seen2=set()
            for j in range(0,9):
                if n[i][j] in seen1:
                    return False
                    break
                else:
                    if n[i][j]!='.':
                        seen1.add(n[i][j])
                if n[j][i] in seen2:
                    return False
                    break
                else:
                    if n[j][i]!='.':
                        seen2.add(n[j][i])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if n[row][col] in seen:
                        return False
                        break
                    else:
                        if n[row][col]!='.':
                            seen.add(n[row][col])
        return True
        