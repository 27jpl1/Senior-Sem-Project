import math
import random
import sys
from scipy.spatial import distance

# A method to find the nearest centroid of a given point
def find_nearest_centroid(centers: list, scores: list):
    closest_center = []                     #Initalizes closest center (This will be replaced)
    closest_distance = sys.maxsize          # Initializes the closest distance to be the max int
    for center in centers:                  # For each centroid, see if it is closer to the document scores and if so make note of it
        euclid_dist = distance.cosine(center, scores)       #Cosine distance as distance metric
        if euclid_dist < closest_distance:
            closest_center = center
            closest_distance = euclid_dist
    return closest_center


# A function to run the k-means clustering algorithm on a set of documents and their idf scores
def k_means_cluster(k: int, data: dict, num_terms: int):
    beginning_centroids = random.sample(data.keys(), k)    # chooses k random centroids
    beginning_centroid_scores = []
    for centroid in beginning_centroids:            # creates a list of the scores for the  beginning centroids
        beginning_centroid_scores.append(data[centroid])
    clusters = {}
    for centroid in beginning_centroids:        # creates a dictionary to hold the items for each cluster
        centroid = tuple(data[centroid])
        clusters[centroid] = []
    for document in data.keys():                          # loops through all document and assigns them to the correct cluster
        clusters[tuple(find_nearest_centroid(beginning_centroid_scores, data[document]))].append(document)
    new_centroids = []
    for centroid in clusters.keys():
        mean = [0] * num_terms              # creates a list of 0s that will be used to find the new centroid
        for document in clusters[centroid]:        # for each document in the cluster,
            for i in range(0, num_terms):    # add each dimension to the mean
                mean[i] += data[document][i]
        for i in range(0, len(mean)):           # divide total dimensions by total documents in cluster
            mean[i] /= len(clusters[centroid])
        new_centroids.append(mean)              # add the mean to the new_centroids
    no_new_assignments = False
    loop = 0
    while not no_new_assignments:               # while the clusters continue changing between runs, continue running the algorithm
        loop += 1
        print("loop: " + str(loop))
        new_centroids, no_new_assignments, clusters = new_cluster(new_centroids, data, num_terms)
    return clusters    # returns the cluster, so they can be analyzed



# A function to run clustering once
# This also checks if there are any new assignments
def new_cluster(centroids: list, data: dict, num_terms: int):
    clusters = {}
    for centroid in centroids:    # creates a dictionary to hold the items for each cluster
        clusters[tuple(centroid)] = []
    for document in data.keys():  # loops through all documents and assigns them to the correct cluster
        clusters[tuple(find_nearest_centroid(centroids, data[document]))].append(document)
    new_centroids = []
    for centroid in clusters.keys():
        mean = [0] * num_terms             # creates a list of 0s that will be used to find the new centroid
        for document in clusters[centroid]:        # for each document in the cluster,
            for i in range(0, num_terms):    # add each dimension to the mean
                mean[i] += data[document][i]
        for i in range(0, len(mean)):           # divide total dimensions by total documents in cluster
            mean[i] /= len(clusters[centroid])
        new_centroids.append(mean)              # add the mean to the new_centroids
    is_same_centroids = True                       # a boolean if the centroids are the same
    for centroid in centroids:
        if centroid in new_centroids:           # if the centroid is part of the new centroids,
            pass                                # then don't change anything
        else:                                   # if the centroid is not part of the new centroids,
            is_same_centroids = False              # then the centroids are not the same
    return new_centroids, is_same_centroids, clusters

# TODO: Kmeans ++ to initialize data
# TODO: Have a return value of the total distance of all points from the centers

