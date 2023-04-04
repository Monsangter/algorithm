def solution(food):
    
    answer = ''
    str1 = ""
    
    ls = []
    
    
    for i in food:
        ls.append(i//2)
        
    print(ls)
    
    for i in range(1,len(ls)):
        str1 += str(i) * ls[i]
        
    answer = str1
    
    answer += "0"
    

    for i in range(1,len(ls)+1):
        answer += str(len(ls)-i) * ls[-i]
    
    print(answer)
    
    
    return answer

#일단 짝수로 만들어 줄 것.
#인덱스에 따라서 음식 번호가 결정. 번호에따른 개수를 정해줘붜자.
