class Solution:
    def twoSum(self,numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(numbers)
        if target%2==0:
            new_target=int(target/2)
            if new_target in numbers:
                index1=numbers.index(new_target)
                if index1<length and numbers[index1]==numbers[index1+1]:
                    return [index1+1,index1+2]
        new_numbers=list(set(numbers))
        length2=len(new_numbers)
        for i in range(length2):
            for j in range(i+1,length2):
                    
                if new_numbers[i]+new_numbers[j]==target:
                    index1=numbers.index(new_numbers[i])
                    index2=numbers.index(new_numbers[j])
                    if index1<index2:
                        return [index1+1,index2+1]
                    else:
                        return [index2+1,index1+1]
                    
                    
