def solution(s):
    upper_list, lower_list = sorted([i for i in s if i.isupper()], reverse=True), \
                             sorted([i for i in s if i.islower()], reverse=True)

    return ''.join(lower_list + upper_list)
