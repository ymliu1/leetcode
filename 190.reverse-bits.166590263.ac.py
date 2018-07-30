class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self,n):
        nstr=bin(n)[2:]
        nlist=list(nstr)
        
        length=len(nlist)
        
        if len(nlist)<32:
                x=32-len(nlist)
                for i in range(x):
                    nlist.insert(0,'0')
        nlist.reverse()
        
        new_number=int(''.join(nlist),2)
        return new_number
