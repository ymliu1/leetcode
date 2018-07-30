class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length=len(s)
        sl=list(s)
        index=[]
        value=[]
        marker=0
        for i in range(length):
            
            if int(i/k)%2==0 and i!=length-1:
                
                index.append(i)
                value.append(s[i])
                marker=0
               
            elif int(i/k)%2!=0 and marker==0:
               
                value.reverse()
                
                for j in range(k):
                    sl[index[j]]=value[j]
                marker=1
                index=[]
                value=[]
            elif i==length-1 and marker==0:
                index.append(i)
                value.append(s[i])
                value.reverse()
                for j in range(len(value)):
                    sl[index[j]]=value[j]
        return ''.join(sl)
                
                
