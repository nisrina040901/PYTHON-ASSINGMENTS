sentence = input('Enter a sentence: ')
new_sentence = sentence.lower()
total = 0

for x in new_sentence:
  if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    total += 1

print(f'Number of vowels = {total}')