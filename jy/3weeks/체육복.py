def solution(n, lost, reserve):
    new_lost = [l for l in lost if l not in reserve]
    new_reserve = [r for r in reserve if r not in lost]

    for r in new_reserve:
        if r - 1 in new_lost:
            new_lost.remove(r - 1)
        elif r + 1 in new_lost:
            new_lost.remove(r + 1)

    return n - len(new_lost)

n = 5
lost = [2, 4]
reserve = [1, 3, 5]

solution(n, lost, reserve)