import random
a=['always','be','yourself'],['keep','it','cool'],['dont','be','nerves']
print(a[random.randint(0,len(a)-1)])
score=0
phrase=['keep','it','cool']
under_ph=['_'*len(word) for word in phrase]
print(phrase)
print(under_ph)
while under_ph != phrase:
 letter=input('enter letter:')
 guess = 0
 for word_index in range(len(phrase)):
    for letter_index in range(len(phrase[word_index])):

        if phrase[word_index][letter_index]==letter:
            under_ph[word_index] = under_ph[word_index][:letter_index] + letter + under_ph[word_index][letter_index+1:]
            guess += 1

 if guess != 0:
     score += 5
 else:
     score -= 1

 print(under_ph)

print(under_ph)
print(score)

