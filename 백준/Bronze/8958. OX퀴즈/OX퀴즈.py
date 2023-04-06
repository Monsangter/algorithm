from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()


  N = int(input())

  sum1 = 0
  for i in range(N):
    
    ls1 = input().split("X")

    for i in ls1:
      for j in range(len(i)):
        sum1 += j+1
    print(sum1)
    sum1 = 0
          


  
if __name__ =="__main__":
  main()