n = int(input("Enter number of marks : "))
total =  0 

for i in range ( n ) : 
    quiz_Mark = float ( input ( " Enter Quiz Marks : "))
total += quiz_Mark 

averange = total / n 
print ( " The averange of the quiz marks is :" , averange )
