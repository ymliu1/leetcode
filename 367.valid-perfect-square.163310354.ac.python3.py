class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count=1
        int_num=1
        count_num=num
        marker=0
        
        num_count=0
        answer_first=1
        answer_second=1
        while count_num!=0:
            count_num=int(count_num/10);
            if count_num>=1:
                count=count+1;
            
        if count<=2:
            for i in range(10):
                if i*i==num:
                    marker=1;
                
            
        if count>2:
            for i in range(count-1):
                int_num=int_num*10;
                
            first_num=int(num/int_num);
    
            if count%2==0:
                num_count=int(count/2);
            elif count%2==1:
                num_count=int(count/2+1);
            print (num_count);
            for i in range(1,10):
                answer_first=i
                answer_second=i+1
                for j in range(num_count-1):
                    answer_first=answer_first*10;
                    
                    answer_second=answer_second*10;
                    
                    
                    if answer_first**2<num and answer_second**2>num: 
                        for i in range(answer_first,answer_second):
                            
                            if i*i==num:
                                marker=1;
                                break;
                    elif answer_first**2==num or answer_second**2==num:
                        marker=1;
                        break;
                    
        if marker==1:
            return True;
        else:
            return False;
