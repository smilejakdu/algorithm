import numpy as np

def solution(answers):
    answer = []
    ans_set = []
    ans_set.append([1,2,3,4,5])
    ans_set.append([2,1,2,3,2,4,2,5])
    ans_set.append([3,3,1,1,2,2,4,4,5,5])
    
    right_ans = []
    for index in range(len(ans_set)):
        count = 0
        for index_a in range(len(answers)):
            if answers[index_a] == ans_set[index][index_a%len(ans_set[index])]:
                count += 1
        right_ans.append(count)
       
    max_ans = max(right_ans)
    answer = [i for i, j in enumerate(right_ans) if j == max_ans]
    answer = [i+1 for i in answer]
    
    #answer.append(int(np.argmax(right_ans))+1)

   
    return answer
