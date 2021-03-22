import re


def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9_.-]", "" ,new_id)
    new_id = re.sub("[.]+",".",new_id)
    
    #if new_id.startswith("."):
    #    new_id = new_id[1 : : ]  
    #if new_id.endswith("."):
    #    new_id = new_id[:-1:]
        
    new_id =new_id.strip(".") #remove "." in the first and the last 
    
    if len(new_id)>15:
        new_id = new_id[:15:]
        if new_id.endswith("."):
            new_id= new_id[:-1:]
    
    #if(len(new_id))==0:
    #    new_id = "aaa"   
        
    new_id = new_id if new_id else "a" #replace a whitespace with "a"

    if len(new_id)<3:
        str_to_add =new_id[-1]
        new_id = new_id.ljust(3, str_to_add)
        
    answer = new_id
    return answer
