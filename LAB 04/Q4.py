weight = int(input("Weight: "))
unit = input('(G)s and (K)gs ')
if unit.upper() == 'G':
    converted = weight
    print(f" You are {converted} grams to kilograms ")
else:
    converted = weight
    print(f"{converted} grams ")

    converted = weight // 1000
    print(f"{converted} kilograms ")