from random import choice
from time import sleep
text, randomcased, truefalse = input('Type the text you want to set to random case: '), '', [True, False]
for x in text:
	if choice(truefalse):
		randomcased = randomcased + x.swapcase()
	else:
		randomcased = randomcased + x
print(f'Final text:\n{randomcased}')
sleep(10)
