def solution(n):
    answer = 0
    sum1 = 0
    
    #공차가 1 인 등차 수열..
    # 개수는 몇개인가..
    
    #첫째항과 마지막항을 더해서.. 항의 갯수만큼 곱한다음... 나누기 2 하는게 일반식.
    #첫째항은 무엇이 되는가.
    #마지막항은 무엇이 되는가.
    # 항이 5개. 가능 왜 4개는 안됨?
    
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             sum1 += j
#             if sum1 == n:
#                 answer += 1
#                 break
            
#         sum1 = 0
                

                
        
    
#     return answer

def solution(n):
    count = 0                      
    for i in range(1, n+1):         # 예시의 `15=15`도 있기 때문에 n+1 까지 반복문 실행
        sumN = 0                     
        for j in range(i, n+1):     # i값을 시작으로 반복문 실행
            sumN += j               # i값부터 계속해서 값을 더해준다
            if sumN == n:           # 더한 값이(sumN)이 n과 같다면 count +1, break
                count += 1          
                break
            if sumN > n:            # 더한 값(sumN)이 n보다 크다면 계산할 필요가 없음
                break
    return count