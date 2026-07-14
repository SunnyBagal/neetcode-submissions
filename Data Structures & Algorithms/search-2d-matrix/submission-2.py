class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)        # 3
        cols = len(matrix[0])     # 4

        for i in range(rows):     # till the length of matrix
          left = 0
          right = cols - 1

          while left <= right:
            middle = (left + right) // 2      #middle value => 0 

            if matrix[i][middle] == target :      #matrix[1][0] == 10 == 10 ?? True
              return True 
            
            elif matrix[i][middle] < target:    #matrix[0][2] == 4 < 10:
              left = middle + 1                 

            else:                         #matrix[1][2] == 12 > 10
              right = middle - 1

        return False
