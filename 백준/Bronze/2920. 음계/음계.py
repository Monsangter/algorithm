from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()

  A = input()

  if A == "1 2 3 4 5 6 7 8":
    print("ascending")
  elif A == "8 7 6 5 4 3 2 1":
    print("descending")
  else:
    print("mixed")

    

  
if __name__ =="__main__":
  main()