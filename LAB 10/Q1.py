# file = open("data.txt")



data = open ('data.txt')
lines = data.readline ()

print(lines)
count = 0 

for line in lines : 
  count += 1

print (f"Line {count} : {line.strip()}")

print ( f'line count : {count}')
print(f"first lines : {lines[0]}" + f"last lines : {lines[-1]}")