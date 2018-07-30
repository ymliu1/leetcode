class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        length1=len(matrix)
        length2=len(matrix[0])
        for i in range(length1-1):
            for j in range(length2-1):
                while matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True
