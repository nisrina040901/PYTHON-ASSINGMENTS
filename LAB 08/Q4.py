lenght = int(input (" Enter list lenght : "))
my_list = []
for _ in range (lenght):
  temp = int(input("Enter List Item : "))
  my_list.append(temp)

samllest = my_list[0]
for item in my_list :
  if item < smallest : 
    smallest = item 

print ("smallest is a list is : " , smallest)
