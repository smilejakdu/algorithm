def solution(s):
    s = s.lower()
    y_count = 0
    p_count = 0
    
    for i in s:
        if i == "y":
            y_count+=1
        elif i =="p":
            p_count+=1
    return y_count == p_count
