mkdir outputbluemix

echo "Naive Implementation based on Frequency count of words: "
python wordfreq.py 

echo "Cosine Similarity: GloVe"
python cosineSimilarity.py > outputbluemix/cosineSimilarityLOG

echo "cosineSimilarity 1"
python cosineSimilarity_1.py > outputbluemix/cosineSimilarityLOG1

python hierarchy.py > outputbluemix/hierarchyclusterLOG

#python colorCode.py
python colorvaccine.py