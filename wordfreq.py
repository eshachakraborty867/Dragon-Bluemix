from collections import defaultdict

count = defaultdict(float)
threshold1 = 2
threshold2 = 5

fp = open('vaccine_bluemix_processed.txt','w')
for line in open('vaccine_bluemix.txt'):
	line = line.strip().lower().replace('.','')
	fp.write(line)

for line in open('vaccine_bluemix_processed.txt'):
	word_list = line.strip().split(" ")
	for word in word_list:
		#if word not in count:
		count[word] += 1

length_actual = len(count)
length_medical = 0.0

for line in open('vaccine_bluemix_processed.txt'):
	word_list = line.strip().split(" ")
	for word in word_list:
		if count[word] > threshold1 and count[word] < threshold2:
		#if count[word] < threshold1:
			#print word, count[word]
			length_medical += 1.0

print (("Percentage of medical text: %f percent")%((length_medical / length_actual)*100))
fp.close()



