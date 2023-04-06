from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()


  S = input()
  ls1 = []

  for i in range(26):
    ls1.append(str(S.find(chr(97 + i))))

  print(" ".join(ls1))
          


  
if __name__ =="__main__":
  main()
