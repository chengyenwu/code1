# 73. Set matrix zeroes
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first append row and column index
        element_list = []
        for i in range(len(matrix)):
            row_num = matrix[i]
            for j in range(len(row_num)):
                if row_num[j] == 0:
                    element_list.append([i, j])
        
        for element in range(len(element_list)):
            h = element_list[element][0]
            v = element_list[element][-1]
            # deal with row
            for i in range(len(matrix[h])):
                matrix[h][i] = 0
            # deal with column
            for j in range(len(matrix)):
                matrix[j][v] = 0