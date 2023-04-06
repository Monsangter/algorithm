from sys import stdin
def main():
  def input():
    return stdin.readline().rstrip()


  str1 = input().upper()
  ls2 = list(set(str1))
  ls3 = []

  a = max(map(str1.count,ls2))
  
  for i in ls2:
    if str1.count(i) == a:
      ls3.append(i)
  
  if len(ls3)>1:
    print("?")
  else:
    print(ls3[0])

if __name__ =="__main__":
  main()