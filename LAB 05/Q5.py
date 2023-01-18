itemprice = int(input (" Enter item price :  "))
tagcolour = (input(" Enter tag colour : "))
membercard = input("Do you have a member card? (Yes /No ): ")
totaldiscount = int(input ( "Total Discount = "))

discount = itemprice * 5/100
if tagcolour == "white":
    if membercard == "Yes":
        itemprice = itemprice * 0.95
    else:
        itemprice = itemprice * 0.95

discount = itemprice * 70/100
if tagcolour == "blue ":
    if membercard == "Yes":
        itemprice = itemprice * 0.30
    else:
        itemprice = itemprice * 0.70

discount = itemprice * 55/100
if tagcolour == " red ": 
    if membercard == "Yes":
        itemprice = itemprice * 0.55
    else:
        itemprice = itemprice * 0.45

discount = itemprice * 30/100
if tagcolour == " yellow ":
    if membercard == "Yes":
        itemprice = itemprice * 0.70
    else:
        itemprice = itemprice * 0.30
print ( "The price of the items :", itemprice )