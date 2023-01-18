import random 



def coin_toss():
    number = random.randrange(1,3)
    if(number==1):
      print(f'{number}:heads')

    else:
      print(f'{number}:tails')

n = int(input('Enter N:'))
for i in range (n):
    coin_toss()