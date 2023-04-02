def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    
    for i in range(len(score) // m):
        answer += score[m-1+(m *i)] * m
        
    return answer

#일단 큰 사과부터 담아야함.
#정렬을 해서 그 인덱스가 최악의 사과가 되겠지.

