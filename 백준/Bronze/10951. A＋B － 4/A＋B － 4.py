from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()


  while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)
          


  
if __name__ =="__main__":
  main()