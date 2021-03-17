'''
학생들의 번호는 체격 순
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려 줄 수 있습니다.
예를들어 , 4번학생은 3번 학생이나 5번 학생에게만 체육복을 빌려 줄수 있다.

- 전체 학생의 수 n 
- 체육복을 도난당한 학생들의 번호가 담긴 배열 lost
- 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reverse
- 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.

output = > 체육수업을 들을 수 있는 학생의 최댓값을 return
'''

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
        if reserve_student[student]==0 and student !=0 and reserve_student[student-1] >1  :
            reserve_student[student]+=1
            reserve_student[student-1]-=1
        elif reserve_student[student]==0 and len(reserve_student) != student+1 and reserve_student[student+1]>1:
            reserve_student[student]+=1
            reserve_student[student+1]-=1

    for student in reserve_student:
        if student >0:
            answer+=1

    return answer
