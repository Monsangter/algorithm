from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  sum1 = 0
  N = int(input())
  a = input()
  for i in a:
    sum1 += int(i)

  print(sum1)
  
if __name__ =="__main__":
  main()