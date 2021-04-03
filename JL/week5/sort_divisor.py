def solution(arr, divisor):
    #list comprehension
    answer = []
    for number in arr:
        if number%divisor == 0:
            answer.append(number)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer
