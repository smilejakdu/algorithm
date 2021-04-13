def solution(seoul):
    for s in range(len(seoul)):
        if seoul[s] == "Kim":
            return f'김서방은 {s}에 있다'
