def armstrong(n):
  rev = 0
  a = 0
  while n > 0:
    rev = (n % 10)
    a = a + rev**3
    n = n // 10
  return a,n
n = int(input())
if armstrong(n) == n: print('armstrong')
else: print('not')
