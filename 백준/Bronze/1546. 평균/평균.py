from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  N = int(input())
  ls1 = list(map(int,input().split()))
  M = max(ls1)
  sum1 = 0

  for i in ls1:
    sum1 += i / M * 100

  print(sum1/N)
  
if __name__ =="__main__":
  main()