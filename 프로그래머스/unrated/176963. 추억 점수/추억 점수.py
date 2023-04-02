def solution(name, yearning, photo):
    answer = []
    dict1 = { key:value for key, value in zip(name, yearning) }
    
    sum1 = 0
    
    for i in photo:
        for j in i:
            if j in dict1:
                sum1 += dict1[j]
        answer.append(sum1)
        sum1 = 0
            
        
    
    #이름이 숫자처럼 작용한다. ! 이름을 먼저 숫자로 만들자 딕셔너리
    
    return answer