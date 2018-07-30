class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        length=len(s);
        list=[]
        list2=[]
        str=''
        str2=''
        for i in range(length):
            if s[i].isalpha() or s[i].isdigit():
                list.append(s[i]);
                list2.append(s[i])
        list.reverse();
        n=len(list);
        for i in range(n):
            str=str+list[i];
            str2=str2+list2[i];
        
        if str2.lower()==str.lower():
            return True;
        else:
            return False;
