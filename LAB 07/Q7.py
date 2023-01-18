p = float(input('Enter principal: RM'))
r = float(input('Enter interest rate %: '))
n = 10

print('Future value after')

while n <= 60:
  f = p * (1 + r/100) ** n
  print(str(n) +' years: RM '+ str('{:,.2f}'.format(f)))
  n += 10