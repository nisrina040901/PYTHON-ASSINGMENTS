n = int(input('Enter N: '))

for x in range(1, n+1):
  print(' ' * (n-x) + '*' * x)