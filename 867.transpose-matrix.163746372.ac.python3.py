class Solution:
    def transpose(self,A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length1=len(A)
        length2=len(A[0])
        list1=[]
      
        
        for j in range(length2):
            list1.append([])
            
            for i in range(length1):
                list1[j].append(A[i][j])
        return list1

