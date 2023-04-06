from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  mul1 = 1
  for i in range(3):
    mul1 *= int(input())

  for i in range(10):
    print(str(mul1).count(str(i)))

    
    

  
if __name__ =="__main__":
  main()