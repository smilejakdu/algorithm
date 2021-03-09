def solution(array, commands):

    answer = []

    for command in commands:#[2,5,3]

        i = command[0]-1
        j = command[1]-1
        k = command[2]-1

        if i == j:
            answer.append(array[i])
        else:
            num_list=[]
            for i in range(i,j+1):
                num_list.append(array[i])
            num_list.sort()
            answer.append(num_list[k])

    return answer
