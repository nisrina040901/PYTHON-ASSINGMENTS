package = int(input("Enter package no: "))
minutes_used = int(input("Enter minutes used: "))

if package == 1:
  if minutes_used <=450:
    total_amount=40
    print("Amount due =", round(total_amount,1))
  else:
    total_amount = 40+((minutes_used-450)*0.45)
    print("Amount due =", round(total_amount,1))

elif package == 2:
  if minutes_used <=900:
    total_amount=60
    print("Amount due =", round(total_amount,1))
  else:
    total_amount = 60+((minutes_used-900)*0.40)
    print("Amount due = RM(total_bill)")

else:
  total_amount=70
  print("Amount due =", round(total_amount,1))