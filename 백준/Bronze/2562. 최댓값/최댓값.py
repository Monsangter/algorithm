from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  ls1 = []
  for i in range(9):
    ls1.append(int(input()))

  print(max(ls1))
  print(ls1.index(max(ls1))+1)

  
if __name__ =="__main__":
  main()