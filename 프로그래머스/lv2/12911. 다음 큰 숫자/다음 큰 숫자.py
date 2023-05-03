def solution(n):
    answer = 0
    
    cnt = bin(n)[2:].count("1")
    
    
    
    while True:
        n += 1
        
        if bin(n)[2:].count("1") == cnt:
            return n
    

#1의 숫자가 일정해야 한다..1의 숫자가 5개인 모든 수의 리스트를 만들 수 있지 않을까?