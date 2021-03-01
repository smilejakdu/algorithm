def solution(numbers):
    answer = []
    for i,val1 in enumerate(numbers):
        for j,val2 in enumerate(numbers):
            if i!=j:
                answer.append(val1+val2)
            answer = list(dict.fromkeys(answer))
    answer.sort()
    return answer
