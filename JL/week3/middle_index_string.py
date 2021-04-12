def solution(s):
    
    answer = []
    if len(s) % 2 == 0 :
        i = int((len(s)/2))
        j = i-1

        answer.append(s[j])
        answer.append(s[i])
        answer = ''.join(answer)
        
    else:
        i = int((len(s)-1)/2)

        answer = s[i]
    return answer
