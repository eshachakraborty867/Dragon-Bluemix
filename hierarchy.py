import numpy as np
import scipy.cluster.hierarchy as hac
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
import nltk

dist=[]
wordlist=[]
stopwords = nltk.corpus.stopwords.words('english')

for line in open('FILES/words_vector.txt'):
	items = line.strip().split(" ")
	wordlist.append(items[0])
	numlist = items[1:]
	dist.append(numlist)


cosdist = np.asarray(dist)
a = ssd.pdist(cosdist, 'cosine')

z = hac.linkage(a, 'average')

#fcluster thresholds z by 0.5 times
#the max of the closest element
arr = hac.fcluster(z, 0.5*max(z[:,2]), 'distance')
uniquearr = set(arr)

fp = open("FILES/words_cluster.txt", 'w')
for uniqueitem in uniquearr:
	fp.write(uniqueitem)
	fp.write("\n")
	for i in xrange(len(arr)):
		if arr[i]==uniqueitem:
			if wordlist[i] not in stopwords:
				fp.write(wordlist[i])
				fp.write("\n")
fp.close()

	