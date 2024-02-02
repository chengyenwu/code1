# 74. Search a 2D matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # dynamic programming method
        dp=[0] * (len(matrix) * len(matrix[0]))
        j=0
        for i in range(len(matrix)):
            row_num = matrix[i]
            for row_element in range(len(row_num)):
                dp[j] = row_num[row_element]
                j+=1
        for k in dp:
            if k == target:
                return True
        return False
    
        # Solution 2.
        # for i in range(len(matrix)):
        #     row_num = matrix[i]
        #     for j in range(len(row_num)):
        #         if row_num[j] == target:
        #             return True
        # return False