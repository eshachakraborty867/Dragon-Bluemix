import math
from collections import defaultdict
from scipy import spatial
import numpy as np

cosine_dict = defaultdict()
for ref_line in open('outputbluemix/cosineSimilarityLOG'):
#for ref_line in open('outputvaccine/cosineSimilarityLOG'):
	ref_line_elements = ref_line.strip().split(" ")
	ref_word = ref_line_elements[0]
	ref_vec = ref_line_elements[1:]
	#print vec[0], vec[1]
	cosine_dict[ref_word] = defaultdict(float)

	for line in open('outputbluemix/cosineSimilarityLOG'):
	#for line in open('outputvaccine/cosineSimilarityLOG'):
		line_elements = line.strip().split(" ")
		word = line_elements[0]
		vec = line_elements[1:]

		ref_vec = np.array(ref_vec, dtype = float)
		vec = np.array(vec, dtype = float)

		if (word != ref_word) and (((1 - spatial.distance.cosine(ref_vec, vec)) - 0.44) >= 0.0):
			cosine_dict[ref_word][word] = 1 - spatial.distance.cosine(ref_vec, vec)
			#cosine_dict[ref_word][word] = cosine_similarity(ref_vec, vec)
			print ref_word, word, cosine_dict[ref_word][word]
			



