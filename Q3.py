number = open('numbers.txt' , 'r')
lines = [int (i) for i in number.readlines()]

max = lines[0]
min = lines[0]
sum = 0.0 

for line in lines: 
  if (line > max): 
    max = line 

  elif( line < min): 
    min = line 

sum+= line

n = len(lines)

print(f'Count = {n}')
print(f"larest = {max}")
print(f"smallest = {min}")

print(f"average = {round(sum/n, 2 )}")
number.close()