def solution(nums):
    result = []
    answer = len(nums) // 2
    nums   = list(set(nums))
    return len(nums) if answer > len(nums) else answer
