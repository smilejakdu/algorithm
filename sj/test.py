import sys

input: () = lambda: sys.stdin.readline().strip()

# 1


def solution_with_backtracking(depth, nums, n, m):
    if depth == m:
        print(*result)
        return

    for i in range(n):
        if not used[i]:
            result.append(nums[i])
            used[i] = True
            solution_with_backtracking(depth + 1, nums, n, m)
            used[i] = False
            result.pop()


def product(repeat=1, *args):
    pools = [tuple(pool) for pool in args] * repeat
    print(pools)
    result = [[]]

    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    print(result)

    for prod in result:
        yield tuple(prod)


# 2
def permutation_with_hardcoding(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))  # [0,1,2,3,4,...,n-1]
    cycles = list(range(n, n - r, -1))  # [n,n-1,n-2,n-3,...,n-r+1]
    yield tuple(pool[i] for i in indices[:r])  # generate first element
    while n:  # if itertool is not None, infinite loop
        for i in reversed(range(r)):
            print(indices)
            # print(cycles)
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:  # every cycles's element is 0
            return

# 3


def permutation_with_product(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r

    for indices in product(r, range(n)):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)


def solution_with_permutation(num_list, r):
    result = permutation_with_product(num_list, r)
    for perm in result:
        print(*perm)


if __name__ == '__main__':
    n, m = map(int, input().split())
    num_list = sorted(list(map(int, input().split())))

    # solution using my_permutation
    # solution_with_permutation(num_list, m)

    # solution using bacltracking
    used = [False for _ in range(n)]
    result = list()
    solution_with_backtracking(0, num_list, n, m)
