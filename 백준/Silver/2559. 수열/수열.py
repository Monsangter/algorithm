from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()
    
  N,K = map(int,input().split())

  ls1= list(map(int,input().split()))
  ls2 = []

  sum1 =0

  #중복되는 값을 줄인다. 

  
  for i in range(K):
    sum1 += ls1[i] 

  
  ls2.append(sum1)
  
  for i in range(N-K):
    ls2.append(ls2[i]-ls1[i]+ls1[i+K])

  print(max(ls2))
  


if __name__ == "__main__":
  main()