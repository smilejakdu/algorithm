'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

정답을 가장 많이 맞힌 사람

answers	        return
[1,2,3,4,5]	    [1]
[1,3,2,4,2]	    [1,2,3]
'''

answers = [1,2,3,4,5]

def solution(answers):

    supo_list    = [[1, 2, 3, 4, 5],
                    [2, 1, 2, 3, 2, 4, 2, 5],
                    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    answer_list  = [0 , 0 , 0]

    for answer in range(len(answers)):
        if supo_list[0][answer % len(supo_list[0])] == answers[answer]:
            answer_list[0] += 1

        if supo_list[1][answer % len(supo_list[1])] == answers[answer]:
            answer_list[1] += 1

        if supo_list[2][answer % len(supo_list[2])] == answers[answer]:
            answer_list[2] += 1

    result_list = [answer+1 for answer in range(0 , len(answer_list)) if max(answer_list) == answer_list[answer]]

    return result_list

print(solution(answers))

