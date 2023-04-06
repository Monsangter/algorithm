from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  N = int(input())

  for i in range(1,N+1):
    print(i)
  
    

  
if __name__ =="__main__":
  main()