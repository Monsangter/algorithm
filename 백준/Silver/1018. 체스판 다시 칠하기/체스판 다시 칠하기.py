from sys import stdin

def main():
  def input():
    return stdin.readline().rstrip()
    
  N,M = map(int,input().split())
  matrix = [input() for i in range(N)]

  w_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
  ]
  b_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
  ]

  def check(i,j):
    result_w = 0
    result_b = 0
    for di in range(8):
      for dj in range(8):
        ni,nj = i+di,j+dj
        if matrix[ni][nj] != w_board[di][dj]:
          result_w += 1
        if matrix[ni][nj] != b_board[di][dj]:
          result_b += 1

    return min(result_w, result_b)

  result = 1000000

  for i in range(N-7):
    for j in range(M-7):
      result = min(result,check(i,j))

  print(result)

  
  
if __name__ == "__main__":
  main()