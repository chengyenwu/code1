# 378. Kth smallest element in a sorted matrix
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Dynamic programming
        dp=[0] * (len(matrix)**2)
        j=0
        for i in range(len(matrix)):
            column_num = matrix[i]
            for column_element in range(len(column_num)):
                dp[j] = column_num[column_element]
                j+=1
        dp.sort()
        return dp[k-1]