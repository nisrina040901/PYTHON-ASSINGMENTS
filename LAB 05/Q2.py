balance = float(input("Enter balance:"))
withdrawal_amount = float(input("Enter withdrawal amount:"))

if balance>withdrawal_amount:
 new_balance = balance-withdrawal_amount
 
 print (" New balance = ", new_balance )

else:
  print ("Withdrawal denied")
