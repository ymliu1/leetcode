class Solution:
    def judgeSquareSum(self,c):
        """
        :type c: int
        :rtype: bool
        """
        d=c**0.5
        
        d=int(c**0.5)
      
        marker=0
        
        for a in range(d+1):
            for b in range((d-a),d+1):
                if marker==1:
                   
                    break
               
                elif a**2+b**2==c:
                    marker=1
                    break
                
                
                
                
        if marker==1:
            return True
        else:
            return False
        

