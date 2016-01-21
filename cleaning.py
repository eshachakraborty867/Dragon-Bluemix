import re
import string

fp = open("FILES/vaccine.csv", 'w')
for line in open("vaccine_unclean.csv"):
	words = line.strip().split(',')
	if words[0] == "WORD" or words[0] == "%HESITATION":
		fp.write(','.join(words))
		fp.write("\n")
		continue
	for c in string.punctuation:
		words[0] = words[0].replace(c,"").lower()
		words[0] = re.sub("\d+","",words[0])
	fp.write(','.join(words))
	fp.write("\n")
fp.close()

fp = open("FILES/vaccine.txt", 'w')
for line in open('FILES/vaccine.csv'):
	words = line.strip().split(',')
	if words[0] == "WORD" or words[0] == "%HESITATION":
		continue
	fp.write(words[0] + " ")
fp.close()