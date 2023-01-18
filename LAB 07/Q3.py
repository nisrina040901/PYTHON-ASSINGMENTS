sentence = input('Enter a sentence: ')
new_sentence = sentence.split(' ')  #turns into a list by splitting the space
i=0

for word in new_sentence:
  i += 1

print(f'Number of words = {i}')