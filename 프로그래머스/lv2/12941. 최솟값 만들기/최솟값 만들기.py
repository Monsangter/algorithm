import math
from itertools import product

def solution(A,B):
    answer = 0
    
    
    ls1 = []
    
    
    
    #각자 쌍을 만들어 곱해 더해주는데, 이게 최소가 돼야 한다.
    #각자의 결과들을 구해서 최소가 되는 값을 찾는다.
    
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        
        answer += A[i] * B[i]
    
    

    return answer