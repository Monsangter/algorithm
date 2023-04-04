def solution(n):
    answer = 0
    sum1 = 0
    
    #공차가 1 인 등차 수열..
    # 개수는 몇개인가..
    
    #첫째항과 마지막항을 더해서.. 항의 갯수만큼 곱한다음... 나누기 2 하는게 일반식.
    #첫째항은 무엇이 되는가.
    #마지막항은 무엇이 되는가.
    # 항이 5개. 가능 왜 4개는 안됨?
    
    for i in range(1,n+1):
        for j in range(i,n+1):
            sum1 += j
            if sum1 == n:
                answer += 1
                break
            elif sum1 > n:
                break
            
            
        sum1 = 0
        
    return answer
                

                
        
    