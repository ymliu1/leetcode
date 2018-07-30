class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        length=len(A)
        length2=len(B)
        if length!=length2:
                return False
        if A=='' and B=='':
            return True
        for i in range(length):
            for j in range(length):
                if B[i]==A[j]:
                    if A[j:length]+A[0:j]==B:
                        return True
        return False
                        
