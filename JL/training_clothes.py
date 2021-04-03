'''

7
[2,4,5,6,7]
[1,3,4,5,6,7]
7
'''


def solution(n, lost, reserve):
    
    
    new_lost = []
    reserve_new = list(set(lost)& set(reserve))
    reserve = list(set(reserve)-set(reserve_new))
    
    new_lost = list(set(lost)-set(reserve_new))
    
    lost_1 = [i+1 for i in new_lost]
    lost_2 = [i-1 for i in new_lost]
    
    new_lost = list(set(lost_1+lost_2))
    
    duplicates = list(set(new_lost) & set(reserve))
    
    if len(duplicates) >= len(lost):
        answer = n
    else:
        answer = n - len(lost) + len(duplicates) +len(reserve_new)
    
    return answer

