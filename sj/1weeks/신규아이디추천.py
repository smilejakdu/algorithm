''':cvar
테스트 1
입력값 〉	"...!@BaT#*..y.abcdefghijklm"
기댓값 〉	"bat.y.abcdefghi"

입력값 〉	"z-+.^."
기댓값 〉	"z--"

입력값 〉	"=.="
기댓값 〉	"aaa"

입력값 〉	"123_.def"
기댓값 〉	"123_.def"

입력값 〉	"abcdefghijklmn.p"
기댓값 〉	"abcdefghijklmn"
'''

test = "...!@BaT#*..y.abcdefghijklm"

import re

def solution(new_id):
    new_id = new_id.lower() # 소문자 
    new_id = re.sub("[^a-z0-9\-_.]","",new_id) # 소문자 '' 

    while ".." in new_id: # 2번이상 연속된 부분을 하나의 마침표로 치환
        new_id = new_id.replace("..",".")

    new_id = new_id.strip(".")
    new_id = new_id if new_id else "a" # 빈 문자열 new_id a 를 대입
    new_id = new_id[:15].rstrip(".")

    if len(new_id) < 3:
        new_id = new_id + new_id[-1] * (3 - len(new_id))

    return new_id

print(solution(test))
