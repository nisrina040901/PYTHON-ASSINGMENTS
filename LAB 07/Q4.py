word = input('Enter a word: ')
new_word = word.lower()
list1 = []
list2 = []

for x in new_word:
  list1.append(x)

for y in new_word[::-1]:
  list2.append(y)

if list1 == list2:
  print(f"'{word}' is a palindrome.")
else:
  print(f"'{word}' is NOT a palindrome.")