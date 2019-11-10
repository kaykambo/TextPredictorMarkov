import numpy as np

#opening text
file = open('bible.txt', 'r') 

#test to make sure text is uploaded correctly
#print file.read()

#make all text lowercase
data = file.read().lower() 

#Testing whether the lowercase worked
#print(data)

cleandata = []

for i in data:
	if ord('a') <= ord(i) <= ord('z'):
		cleandata.append(i)
	else:
		cleandata.append(' ')


#turn into string		
cleandata = ''.join(cleandata)

#testing
#print(cleandata)

cleandata = cleandata.split(' ')
#print(cleandata)

#removing empty spaces from dataset
finaldata = []
for word in cleandata:
	if word != '':
		finaldata.append(word)

#print(finaldata)

d = dict()

#making two lists. 
#a list of words that appear after a specific word
#another for the counts of how many times that word appears after that word

for i, word in enumerate(finaldata[:-1]):
	if word in d:
		#if found, adding one to count
		if finaldata[i+1] in d[word][0]:
			j = d[word][0].index(finaldata[i+1])
			d[word][1][j]+=1
		else:
			#if not found, initializing count
			d[word][0].append(finaldata[i+1])
			d[word][1].append(1)
	else:
		#initializes lists for following words
		d[word] = [[finaldata[i+1]], [1]]

#print(d['pipe'])	

#changing our counts to probabilities
for key, value in d.items():
	tot = sum(value[1])
	
	tempprobs = []
	
	for c in value[1]:
		#gotta use floats or it'll just zero out
		tempprobs.append(float(c)/float(tot))
		
	d[key] = [value[0], tempprobs]

#print(d['pipe'])

def conandoyle(prompt, n, dict):
	out = [prompt]
	
	while len(out) <= n:
		choices,probs = dict[out[-1]]
		#print(probs)
		#print(choices)
		choice = np.random.choice(choices, p = probs)
		
		out.append(choice)
		
	
	return ' '.join(out)

print(conandoyle('sin', 100, d))












