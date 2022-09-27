class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            res = [''] * numRows
            row = 0
            down = False

            for ch in s:
                res[row] += ch
                if row == 0 or row == numRows - 1:
                    down = not down
                row += 1 if down else -1

            return ''.join(res)
