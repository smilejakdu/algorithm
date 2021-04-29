'''
이거 풀이 틀림.
'''

def solution(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    answer = 0
    for n in range(2,n+1):
        for i in range(2,n):
            if n % i==0:
                break
        else:
            answer+=1
    return answer
