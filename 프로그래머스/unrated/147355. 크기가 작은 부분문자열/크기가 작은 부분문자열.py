def solution(t, p):
    answer = 0
    cnt = 0
    
    # 슬라이싱해서 그 길이만큼 본다.
    
    
    for i in range(0,len(t)-len(p)+1):
        if int(p) >= int(t[i: i+len(p)]):
            cnt += 1
    

    return cnt