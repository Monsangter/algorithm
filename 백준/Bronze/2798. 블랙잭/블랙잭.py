from sys import stdin
from itertools import combinations

def main():
  def input():
    return stdin.readline().rstrip()
    
  N,M = map(int,input().split())

  ls1= list(map(int,input().split()))

  ls2 = combinations(ls1 , 3)

  tmp = 0
  pro = 300000

  for i in ls2:
    if M - sum(i)< pro and sum(i) <= M:
      tmp = sum(i)
      pro = M-sum(i)

  print(tmp)
  
if __name__ == "__main__":
  main()