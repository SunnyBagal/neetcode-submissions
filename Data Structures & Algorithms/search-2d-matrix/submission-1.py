class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)        # 3
        cols = len(matrix[0])     # 4

        for i in range(rows):
          left = 0
          right = cols - 1

          while left <= right:
            middle = (left + right) // 2

            if matrix[i][middle] == target :
              return True 
            
            elif matrix[i][middle] < target:
              left = middle + 1

            else: 
              right = middle - 1

        return False
