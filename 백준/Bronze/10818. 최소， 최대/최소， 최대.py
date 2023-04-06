from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()


  N = input()
  ls1 = list(map(int,input().split(" ")))

  print(min(ls1), max(ls1))
          


  
if __name__ =="__main__":
  main()
