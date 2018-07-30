class Solution:
    def validPalindrome(self,s):
        """
        :type s: str
        :rtype: bool
        """
        length=len(s);
        list=[]
        list2=[]
        
        
        for i in range(length):
            if s[i].isalpha() or s[i].isdigit():
                list.append(s[i]);
                list2.append(s[i])
        list.reverse();
        n=len(list);
        
        if list==list2:
            return True;
        
        if list!=list2:
            if list[1:n]==list2[0:n-1]:
                return True
            elif  list2[1:n]==list[0:n-1]:
                
                return True
                
            for i in range(n):
                if list[i]!=list2[i]and i!=0:
                    if list[0:i]+list[(i+1):n]==list2[0:n-i-1]+list[(n-i):n]:
                        return True
                    elif  list2[0:i]+list2[(i+1):n]==list[0:n-i-1]+list[(n-i):n]:
                        return True
                    else:
                        return False
                if list[i]!=list2[i]and i!=0:
                    if list[1:n]==list2[0:n-1]:
                        return True
                    elif  list2[1:n]==list[0:n-1]:
                        return True
                    else:
                        return False
                    
                        
        
                    
                    
