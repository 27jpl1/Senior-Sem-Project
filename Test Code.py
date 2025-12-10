import K_Means_Clustering
import TFIDF
import sys

document = open("Who Wrote The Bible Combinations/All Verses", "r")
scores, num_terms = TFIDF.tfidf(document.readlines())
print("before clustering")
best_clusters = []
best_dist = sys.maxsize
for i in range(0, 1):
    print("test:", i)
    clusters, dist = K_Means_Clustering.k_means_cluster(4, scores, num_terms)
    print(dist)
    for key in clusters.keys():
        print(clusters[key])
    if dist < best_dist:
        best_clusters = clusters
        best_dist = dist
print()
for key in best_clusters.keys():
    print(best_clusters[key])
print(best_dist)