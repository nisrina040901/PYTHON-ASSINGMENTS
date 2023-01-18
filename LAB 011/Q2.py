import math 

def findRoot(a,b,c):
  n1=b**2 - 4*a*c
  if(n1<0):
    print('No roots.')
  
  else:
    n2 = math.sqrt(n1)
    r1 = (-b + n2 )/ (2*a)
    r2 = (-b - n2)/ (2*a)
    if(r1==r2):
      print(f'One root : {r1}')
    else :
      print(f'Two roots: {r1} and {r2}')

s = input('Enter a , b, c:')  
n = [int(i) for i in s.split()]
findRoot(n[0],n[1],n[2])