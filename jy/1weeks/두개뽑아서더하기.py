from itertools import combinations

def solution1(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


def solution2(numbers):
    answer = []
    l = list(combinations(numbers, 2))
    print(l)
    for i in l:
        answer.append(i[0]+i[1])
    return sorted(list(set(answer)))

numbers = [5, 0, 7, 9]

print(solution1(numbers))
print(solution2(numbers))
