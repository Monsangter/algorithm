from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()
    
  x,y,w,h = map(int,input().split())
  
  print(min(x,y,w-x,h-y))
  
if __name__ == "__main__":
  main()