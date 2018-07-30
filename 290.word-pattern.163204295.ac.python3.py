class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic_pattern={}
        array_s=[]
        dic_value=[]
        array_s=re.split(r' ',str);
        length=len(pattern);
        if len(array_s)!=length:
            return False;
        for i in range(length):
            if pattern[i] not in dic_pattern:
                
                dic_pattern[pattern[i]]=array_s[i];
                if array_s[i] in dic_value:
                    return False;
                elif array_s[i] not in dic_value and i<length-1:
                    dic_value.append(array_s[i]);
                elif array_s[i] not in dic_value and i==length-1:
                    return True;
                    
            elif pattern[i] in dic_pattern:
                if dic_pattern[pattern[i]]==array_s[i] and i<length-1:
                    continue;
                elif dic_pattern[pattern[i]]==array_s[i] and i==length-1:
                    return True;
                elif dic_pattern[pattern[i]]!=array_s[i]:
                    return False
            else:
                return True;
            
            
            
                
        
        
