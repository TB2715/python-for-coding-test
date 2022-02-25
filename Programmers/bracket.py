from collections import deque


def split(list_w):
    lb = 0
    rb = 0
    
    for idx, ab in enumerate(list_w):
        
        if ab == '(':
            lb += 1
            
        else: 
            rb += 1
            
        if lb == rb:
            return list_w[:idx+1], list_w[idx+1:]
        

def isPerfect(list_u):
    queue = deque()
    
    for ab in list_u:
        if ab == '(':
            queue.append(ab)
        else:
            queue.pop()
        
    if queue:
        return True
    else:
        return False


def make_perfect_bracket(list_u):
    pass
    
    
def sequence(w: list):
    if w == '':
        return w
    else:
        list_u, list_v = split(w)
        
        if isPerfect(list_u):
            return list_u.extend(sequence(list_v))
        
        else:
            make_perfect_bracket(list_u, sequence(list_v))
        
    
    
    

def solution(p):
    return p
    
            
        
        
        
        