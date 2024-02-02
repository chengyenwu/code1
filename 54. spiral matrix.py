# 54. Spiral matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # four pointer (left、right、top、bottom)
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        result = []
        
        while left < right and top < bottom:
            # deal with the top side row (from left to right)
            result += matrix[top][left:right+1]
            # deal with the right side column (from top to bottom, and there is no corner point)
            for i in range(top+1, bottom):
                result.append(matrix[i][right])
            # deal with the bottom side row (from right to left)
            result += matrix[bottom][left:right+1][::-1]
            # deal with the left side column (from bottom to top, and there is no corener point)
            for i in range(bottom-1, top, -1):
                result.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        # consier left = right (only left one column, and should contain corner)
        if left == right:
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
        # considertop = bottom (only left one row, and should contain corner)
        elif top == bottom:
            result += matrix[top][left:right+1]
        return result