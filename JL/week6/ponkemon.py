def solution(nums):
    answer = 0
    poke_list = []
    poke_num = int(len(nums)/2)

    dif_num = len(set(nums))
    if dif_num > poke_num:
        return poke_num
    else:
        return dif_num
