from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  T = int(input())
  
  answer = ""
  
  for i in range(T):
    R, S = input().split()
    R = int(R)
    for i in S:
      answer += i *R

    print(answer)
    answer = ""
    

  
if __name__ =="__main__":
  main()