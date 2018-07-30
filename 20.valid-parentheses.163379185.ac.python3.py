class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_dic={
            '(':')',
            '[':']',
            '{':'}',
        };
        key_list=[]
        length=len(s)
        for i in range(length):
            if s[i] in char_dic:
                key_list.append(s[i])
            elif s[i] not in char_dic:
                if key_list!=[] and char_dic[key_list[-1]]==s[i]:
                        key_list.pop()
                else:
                    return False;
        if key_list==[]:
            return True
        if key_list!=[]:
            return False
 
                        
                    
                    
            
