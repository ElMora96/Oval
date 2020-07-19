import collections as cl
from random import randrange
#Open file
data = open("2018-7.in", 'r')
T = int(data.readline()) #First line of file is T

#Function to generate new words, given a list of positional counters
def generate_word(counter_list):
	new_word = "" #empty string
	L = len(counter_list)
	for j in range(L):
		rand_i = randrange(sum(counter_list[j].values())) #random index -> speeds up execution
		new_char = list(counter_list[j].elements())[rand_i] #extract from counter
		counter_list[j].subtract(new_char) #update counter values
		new_word += new_char #Add char to word
	
	return new_word

#Iterate over test sets
for test in range(T):
	parameters = data.readline().split()
	#Extract parameters N and L
	N = int(parameters[0])
	L = int(parameters[1])
	#List of Vincent's words
	vincent_words = [data.readline().strip() for i in range(0, N)]
	#Build positional counters
	counters = []

	for j in range(L):
		counters.append(cl.Counter())
		for word in vincent_words:
			counters[j].update(word[j])	
	#Look for solution
	w_count = 0 
	flag_found = False
	while w_count < N:
		#print(w_count)
		solution = generate_word(counters)
		w_count += 1
		if not(solution in vincent_words):
			flag_found = True #A valid solution is found
			break

	if not(flag_found):
		solution = "-" #Default solution if no word is found
	#Output
	print("Case #{}: {}".format(test + 1, solution))
