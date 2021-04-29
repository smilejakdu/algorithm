# arr           	answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]   	[4,3]

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer
arr = [1,1,3,3,0,1,1]
# solution(arr)
print(solution(arr))