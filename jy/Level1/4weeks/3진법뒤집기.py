def solution(n):
    t = []
    answer = 0
    while n >= 1:
        t.append(int(n % 3))
        n /= 3
    t.reverse()

    for i in range(len(t)):
        answer += t[i] * (3 ** i)
    return answer


"""
 3 45
 3 15 ... 0
 3  5 ... 0
    1 ... 2
"""
n1 = 45     # 7
n2 = 125    # 229
# solution(n2)
print(solution(n2))