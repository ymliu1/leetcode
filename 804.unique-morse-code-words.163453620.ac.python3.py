class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict_letters={
            "a":".-",
            "b":"-...",
            "c":"-.-.",
            "d":"-..",
            "e":".",
            "f":"..-.",
            "g":"--.",
            "h":"....",
            "i":"..",
            "j":".---",
            "k":"-.-",
            "l":".-..",
            "m":"--",
            "n":"-.",
            "o":"---",
            "p":".--.",
            "q":"--.-",
            "r":".-.",
            "s":"...",
            "t":"-",
            "u":"..-",
            "v":"...-",
            "w":".--",
            "x":"-..-",
            "y":"-.--",
            "z":"--..",
        }
        final_list=[]
        length=len(words)
        
        for i in range(length):
            w_str=""
            trans=[]
            for j in range(len(words[i])):
                trans.append(dict_letters[words[i][j]])
            w_str=w_str.join(trans)
            
            if w_str not in final_list:
                final_list.append(w_str)
        final_len=len(final_list)
        return final_len
                
        
