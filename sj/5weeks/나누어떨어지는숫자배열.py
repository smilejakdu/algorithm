def solution(arr, divisor):
    result = sorted([a for a in arr if a % divisor==0])
    if not result:
        return [-1]

    return result
