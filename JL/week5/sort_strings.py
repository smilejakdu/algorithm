def solution(strings, n):
    answer = []

    strings = sorted(strings)
    sort_d = {}

    for index in range(len(strings)):
        sort_d[index] = strings[index][n]


    sort_d = {key: value for key, value in sorted(sort_d.items(), key=lambda item: item[1])}
    for key in sort_d:
        answer.append(strings[key])


    return answer
