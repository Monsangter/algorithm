from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  A,B = input().split()

  A = int("".join(reversed(A)))
  B = int("".join(reversed(B)))

  print(max(A,B))

    

  
if __name__ =="__main__":
  main()