import sys
input = sys.stdin.readline

N, M = map(int,input().split())
ls1 = list(map(int,input().split()))



for i in range(N-1):
    ls1[i+1] += ls1[i]
    
ls1 = [0] + ls1

for k in range(M):
    i,j = map(int,input().split())
    print(ls1[j]-ls1[i-1])