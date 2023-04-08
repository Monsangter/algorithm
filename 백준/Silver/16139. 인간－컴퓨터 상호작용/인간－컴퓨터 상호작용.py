from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()
    
  S = input()
  q = int(input())

  cnt = 0
  ls1 = []
  tmp = []
  result = 0

  for i in range(26):
    ls1.append([0])
  

  
  
  for i in range(26):
    for j in S:
      if j == chr(97+i):
        cnt += 1
      ls1[i].append(cnt)
    cnt = 0

        

  for i in range(q):
    tmp = input().split()
    result = ls1[ord(tmp[0])-97][int(tmp[2])+1] -ls1[ord(tmp[0])-97][int(tmp[1])]

    print(result)

    
  
if __name__ == "__main__":
  main()