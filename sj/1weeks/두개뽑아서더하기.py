'''
numbers	result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]

정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

numbers = [2, 1, 3, 4, 1]


# 첫번째 문제풀이
def solution(numbers):
    result = []

    for index in range(len(numbers)):
        for index2 in range(index + 1, len(numbers)):
            if numbers[index] + numbers[index2] not in result:
                result.append(numbers[index] + numbers[index2])

    return sorted(result)


# 두번째 문제풀이

# def solution(numbers):
#    answer = []
#    [answer.append(numbers[number1] + numbers[number2]) for number1 in range(0, len(numbers)) for number2 in
#     range(number1, len(numbers)) if number1 != number2 and numbers[number1] + numbers[number2] not in answer]
#    return sorted(answer)

#print(solution(numbers))
