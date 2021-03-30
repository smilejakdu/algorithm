def solution1(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return sorted(answer)


def solution2(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
