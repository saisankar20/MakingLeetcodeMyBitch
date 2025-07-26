class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix), len(matrix[0])
        zr = set()
        zc = set()

        # First pass: just collect zero positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zr.add(i)
                    zc.add(j)

        # Second pass: zero out cells based on recorded rows/columns
        for i in range(rows):
            for j in range(cols):
                if i in zr or j in zc:
                    matrix[i][j] = 0
