def solution(nums):
    select = len(nums)/2
    _nums = list(set(nums))
    if len(_nums) >= select:
        return select
    else:
        return len(_nums)