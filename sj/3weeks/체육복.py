n       = 5
lost    = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    reserve_student = [2 if i in reserve else 1 for i in range(1, n+1)]
    answer =0

    for i,v in enumerate(reserve_student):
        if i+1 in lost:
            reserve_student[i] -= 1

    for student in range(len(reserve_student)):
        if reserve_student[student]==0 and student !=0 and reserve_student[student-1] > 1  :
            reserve_student[student]+=1
            reserve_student[student-1]-=1
        elif reserve_student[student]==0 and len(reserve_student) != student+1 and reserve_student[student+1]>1:
            reserve_student[student]+=1
            reserve_student[student+1]-=1

    for student in reserve_student:
        if student > 0:
            answer+=1

    return answer
print(solution(n , lost , reserve))
