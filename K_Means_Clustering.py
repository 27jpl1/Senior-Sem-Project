import random
import sys
from scipy.spatial import distance

# A function to initialize the centroids using k-means++
def k_means_plus_plus(data_points: list, k:int):
    current_centroid = random.choice(data_points)       # randomly select the first centroid
    centroids = [current_centroid]                      #a list of all centroids chosen
    while len(centroids) < k:                           # while k centroids have not been chosen, chose another
        distances = {}
        for point in data_points:                       # Find the smallest distance to any current centroid and square it
            temp_dist = sys.maxsize
            for centroid in centroids:
                dist_to = distance.cosine(point, centroid)
                if dist_to < temp_dist:
                    temp_dist = dist_to
            distances[tuple(point)] = temp_dist ** 2
        total = sum(distances.values())                 # Find the total distance to create probabilities
        probabilities = []
        for point in data_points:                       # Create a list of probabilities
            probabilities.append(distances[tuple(point)] / total)
        centroids.append(random.choices(data_points, weights=probabilities, k=1)[0])       #Chose a new centroid based on the probabilities
    return centroids


# A method to find the nearest centroid of a given point
def find_nearest_centroid(centers: list, scores: list):
    closest_center = []                     #Initalizes closest center (This will be replaced)
    closest_distance = sys.maxsize          # Initializes the closest distance to be the max int
    for center in centers:                  # For each centroid, see if it is closer to the document scores and if so make note of it
        cos_dist = distance.cosine(center, scores)       #Cosine distance as distance metric
        if cos_dist < closest_distance:
            closest_center = center
            closest_distance = cos_dist
    return closest_center


# A function to run the k-means clustering algorithm on a set of documents and their idf scores
def k_means_cluster(k: int, data: dict, num_terms: int):
    new_centroids = k_means_plus_plus(list(data.values()), k)
    no_new_assignments = False
    loop = 0
    while not no_new_assignments:               # while the clusters continue changing between runs, continue running the algorithm
        loop += 1
        print("loop: " + str(loop))
        new_centroids, no_new_assignments, clusters = new_cluster(new_centroids, data, num_terms)
    total_distance = 0          # records the total distance between each point and its centroid
    for centroid in clusters.keys():
        for document in clusters[centroid]:
            total_distance += distance.cosine(centroid, data[document])
    return clusters, total_distance    # returns the clusters and total_distance, so they can be analyzed



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