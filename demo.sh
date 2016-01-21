mkdir FILES

echo "\n"
echo "Cleaning data..."
python cleaning.py

echo "\n"
echo "Cosine Similarity: GloVe - Take the GloVe vectors and write those vectors (to words_vector.txt) which are of importance to the current document."
python cosineSimilarity.py

echo "\n"
echo "cosineSimilarity - Compute the cosine distances between the word vector under consideration and threshold them"
python cosineSimilarity_1.py

echo "\n"
echo "hierarchical clustering - average clustering to bring similar words together"
python hierarchy.py

echo "\n"
echo "Preparing the HTML document : color code the cluster about vaccine"
python colorvaccine.py