from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  ls1 = list(map(int,input().split()))
  sum1 = 0
  
  for i in ls1:
    sum1 += i ** 2 

  print(sum1%10)
  
if __name__ =="__main__":
  main()