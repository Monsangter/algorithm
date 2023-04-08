from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  while True:
    a,b,c = map(int,input().split())

    if a == 0:
      break
      
    
    if max(a,b,c) ** 2 == a ** 2 + b ** 2 + c ** 2 - max(a,b,c) ** 2:
      print("right")
    else:
      print("wrong")
    

      

  
if __name__ == "__main__":
  main()