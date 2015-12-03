#pirate = {"hotel": "fleabag inn", "boy": "matey" }

sentence = raw_input("write a sentence: ")
sentence = sentence.split(" ")

#for key in pirate:
#	replace key with value,

english = ['sir','hotel', 'student', 'boy','madam','professor','restaurant','your','excuse','student','are','lawyer','the','restroom','my','hello','is','man']
pirate = ['matey','fleabag inn','swabbie','matey','proud beauty','foul blaggart','galley','yer','arr','swabbies','be','foul blaggart','th', 'head', 'me','avast','be','matey']

for word in sentence:
	if word in english:
		index = english.index(word)
		print pirate[index],
	else:
		print word,

#if (english[0] in sentence):
#	replace (pirate [0])