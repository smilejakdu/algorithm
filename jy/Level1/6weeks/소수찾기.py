def is_prime(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def solution(n):
    count = []
    for i in range(2, n+1):
        if is_prime(i):
            count.append(i)
    return len(count)


def solution2(n):
    sieve = [False, False] + [True] * (n - 1)
    count = 0

    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return count

