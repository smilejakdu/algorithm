def solution(a,b):
    answer = 0
    nums   = sorted([a,b])

    for num in range(nums[0],nums[1]+1):
        answer += num

    return answer
