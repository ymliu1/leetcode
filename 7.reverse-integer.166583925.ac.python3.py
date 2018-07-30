class Solution:
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        number=0
        if x>0 and x<2147483647:
                number=reverse1(x)

        if x<0 and x>-2147483648:
                x=-x
                number=reverse1(x)*(-1)
        if x==0 or x>2147483647 or x<-2147483648:
                number=0

        return number
def reverse1(x):
        nlist=[]
        number=0
        while x!=0:
                y=x%10
                x=int(x/10)
                nlist.append(y)
                
        length=len(nlist)
        for i in range(length):
                nlist[i]=nlist[i]*10**(length-i-1)
                number=number+nlist[i]
        if number>2147483647 or number<-2147483648:
            number=0
        return number
        
