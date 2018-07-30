class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a!= 0:
            c = b & a
            b = b ^ a 
            a = c << 1             
        return b
        
