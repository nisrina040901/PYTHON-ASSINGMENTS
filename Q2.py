vehicles = open('vehicles.txt' , 'r')
lines = vehicles.readline()
count = 0 

for line in lines:
  if(line.find('car')!=-1):
    count += 1 
print(f'"car"count: {count}')    
vehicles.close()    