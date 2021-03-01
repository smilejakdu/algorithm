import re

def solution(new_id):
    # stage 1
    new_id = new_id.lower() 
    
    # stage 2
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id) 
    
    # stage 3
    # new_id = re.sub(r'((.)\2+)', '.', new_id)
    new_id = re.sub(r'[.]{2,}', '.', new_id)    
    
    # stage 4
    new_id = re.sub('^[.]', '', new_id)   
    new_id = re.sub('[.]$', '', new_id)
    
    # stage 5
    if new_id == '':    
        new_id = 'a'
        
    # stage 6
    if len(new_id) >= 16:   
        new_id = new_id[:15]
        if new_id[-1] == '.':
            # new_id[-1] = ''
            new_id = new_id[:-1]
    
    # stage 7
    if len(new_id) <= 2:    
        while True:
            if len(new_id) == 3:
                break
            new_id += new_id[-1]
            
    answer = new_id
    return answer