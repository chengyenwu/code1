# 240. Search a 2D matrix II
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row_num = matrix[i]
            for j in range(len(row_num)):
                if row_num[j] == target:
                    return True
        return False