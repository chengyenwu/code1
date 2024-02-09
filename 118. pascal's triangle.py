# 118. Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        numrows = 5
        pascallist=[]
        for i in range(1, numrows+1):
            row=[]
            C=1 # first element is always 1
            for j in range(1, i+1):
                row.append(C)
                C = C*(i-j)//j
                print(i, j, C)
            pascallist.append(row)
        print(pascallist)