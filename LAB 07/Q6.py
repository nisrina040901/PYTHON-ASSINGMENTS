n = int(input('Enter N: '))
x = round(n/2)
y = 1

while x > 0:
  print(' ' * x + '*' * y + ' ' * x)
  y += 2
  x -= 1