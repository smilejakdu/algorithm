def solution(n):

    d = 0
    number = []
    answer = 0
    while (n>=3):
        d = n%3
        n = n//3
        number.append(d)
        
    number.append(n)

    number.reverse()
    for i in range(len(number)):
        answer += number[i] * (3 **i)
        
      
    return answer
