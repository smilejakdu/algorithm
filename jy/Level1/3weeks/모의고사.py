def solution(answers):
    answer = []
    # 1, 2, 3, 4, 5 (5개)
    # 2, 1, 2, 3, 2, 4, 2, 5 (8개)
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 (10개)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1, count2, count3 = 0, 0, 0

    for i in range(len(answers)):
        if one[i % 5] == answers[i]: count1 += 1
        if two[i % 8] == answers[i]: count2 += 1
        if three[i % 10] == answers[i]: count3 += 1

    temp = [count1, count2, count3]
    for person, score in enumerate(temp):
        if score == max(temp):
            answer.append(person + 1)
    return answer


answers = [1, 2, 3, 4, 5]

print(solution(answers))
