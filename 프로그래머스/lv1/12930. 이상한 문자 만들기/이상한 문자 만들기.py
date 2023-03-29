def solution(s):
    answer = ''
    ls = s.split(' ')
    ls2 = []
    tmp = ''
    
    for i in range(len(ls)):
        tmp = ''
        for j in range(len(ls[i])):
            
            if j % 2 == 0 :
                tmp += ls[i][j].upper()
            else:
                tmp += ls[i][j].lower()
                
                
        ls2.append(tmp)
            
        
    answer = " ".join(ls2)

    
    
    return answer