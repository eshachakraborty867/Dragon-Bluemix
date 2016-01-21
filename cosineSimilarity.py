import math
from collections import defaultdict

list1=[]
for line in open('FILES/vaccine.txt'):
	words = line.strip().split(" ")
	for word in words: 
		list1.append(word)
unique_words=set(list1)

fp = open("FILES/words_vector.txt", 'w')
for word in unique_words:
	for ref_line in open('GLOVEdata/vectors.6B.50d.txt'):
		ref_line_elements = ref_line.strip().split(" ")
		ref_word = ref_line_elements[0]
		ref_vec = ref_line_elements[1:]
		if ref_word == word:
			fp.write(ref_line.strip())
			fp.write("\n")
fp.close()
		



