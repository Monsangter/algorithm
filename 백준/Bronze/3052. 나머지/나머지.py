from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  ls1 = []
  
  for i in range(10):
    ls1.append(int(input()) % 42)

  print(len(set(ls1)))

  
if __name__ =="__main__":
  main()