def solution(number, limit, power):
    answer = 0
    cnt = 0
    
    ls = []
    
    #일단 제시된 number까지, 각 순서들은 그 약수 개수를 가지고 있어야함.
    #그러면 일단 그 범위의 모든 자연수에 대해 약수개수를 리스트로 가지자.
    #그리고 그걸 모드 썸!
    
    for i in range(1,number+1):
        for j in range(1,int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
        
        if int(i ** 0.5) != (i** 0.5):
            cnt = cnt * 2
        else:
            cnt = cnt * 2 -1
            
        if cnt > limit:
            cnt = power
            
        ls.append(cnt)
        
        cnt = 0
    
    answer = sum(ls)
    
    
    
    return answer