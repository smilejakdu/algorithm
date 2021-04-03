'''
자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.

입출력 예
n	    result
45	    7
125	    229

'''

def three_number_change(n):
    answer=""
    while n // 3 >=1:
        remain = n % 3
        n = n // 3
        answer = str(remain) + answer
        if n < 3:
            answer = str(n) + answer
    print(answer)
    return answer

def ten_number_change(n):
    answer = 0
    number = 0
    for i in n[::-1]:
        answer += (3**number)*int(i)
        number += 1
    return answer

def solution(n):
    if n < 3:
        return 1
    answer = three_number_change(n)
    answer = ten_number_change(str(int(answer[::-1])))
    return answer

print(solution(45))
