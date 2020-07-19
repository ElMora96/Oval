#EXERCISE 1
def spam_egg():
	for i in range(1,21):
		#Cases
		if (i % 3 == 0) and  (i % 5 != 0):
			print("Spam")
		elif (i % 3 != 0) and (i % 5 == 0):
			print("Egg")
		elif (i % 3 == 0) and (i % 5 ==0):
			print("SpamEgg")
		else:
			print("Number ", i)

spam_egg()
