class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row , cols = len(matrix) , len(matrix[0])
        left , right = 0 , row * cols - 1

        while left <= right:
            mid = (left + right)//2
            row, col = divmod(mid, cols)
            midval = matrix[row][col]

            if midval == target:
                return True
            elif midval < target:
                left = mid + 1
            else:
                right = mid - 1

        return False



        

        

        
