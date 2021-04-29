import math
def solution(n):
    flag = False
    answer = 0
    
    for num in range(2,n+1):
        for divisor in range(2,math.floor(math.sqrt(num))+1):
            if(num%divisor==0):        
                break
        else:
            answer+=1
    
    return answer
