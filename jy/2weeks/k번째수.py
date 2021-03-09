def solution1(array, commands):
    answer = []
    start, end, k = [], [], []

    for command in commands:
        start.append(command[0])
        end.append(command[1])
        k.append(command[2])

    for i in range(len(commands)):
        answer.append(sorted(array[start[i] - 1:end[i]])[k[i] - 1])

    return answer


def solution2(array, commands):
    answer = []

    for command in commands:
        answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return answer


def solution3(array, commands):
    # lambda 인자: 표현식
    # map(함수, 리스트)
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# result = [5, 6, 3]

solution3(array, commands)
