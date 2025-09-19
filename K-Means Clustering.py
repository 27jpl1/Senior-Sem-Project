import random

# A method to find the nearest centroid of a given point
# TODO: finish this method then k-means should be finished
def find_nearest_centroid(centers: list, data_point):
    print("Hi")

# TODO: Figure out how to store data (I think have a separate dictionary with idf scores to document names is best
# A function to run the k-means clustering algorithm
# Note: I am not sure what the date list will be. It may be just a list of lists of idf scores,
# or it may be a list of lists that includes the document name (i.e. Genesis 1-2).
# I could also have a dictionary alongside the data (where the data is just the name of the document,
# and the dictionary maps document name to idf scores.
# It may be best to have data as list of lists of idf scores,
# and a dictionary where the keys or the list of idf scores and the values are document names
# The last idea probably is best so there is much less lookup (only at the end)
def k_means_cluster(k: int, data: list):
    beginning_centroids = random.sample(data, k)    # chooses k random centroids
    clusters = {}
    for centroid in beginning_centroids:        # creates a dictionary to hold the items for each cluster
        clusters[centroid] = []
    for point in data:                          # loops through all data points and assigns them to the correct cluster
        clusters[find_nearest_centroid(beginning_centroids, point)].append(point)
    new_centroids = []
    for centroid in clusters.keys():
        # This line may need to change depending on what data is
        mean = [0] * len(data[0])               # creates a list of 0s that is as long as the length of each data point
        for point in clusters[centroid]:        # for each data point in the cluster,
            for i in range(0, len(data[0])):    # add each dimension to the mean
                mean[i] += point[i]
        for i in range(0, len(mean)):           # divide total dimensions by total points in cluster
            mean[i] /= len(clusters[centroid])
        new_centroids.append(mean)              # add the mean to the new_centroids
    no_new_assignments = False
    while not no_new_assignments:               # while the clusters continue changing between runs, continue running the algorithm
        new_centroids, no_new_assignments, clusters = new_cluster(new_centroids, data)
    return clusters    # returns the cluster, so they can be analyzed (can use dictionary to convert them to their document names



# A function to run clustering once
# This also checks if there are any new assignments
def new_cluster(centroids, data):
    clusters = {}
    for centroid in centroids:    # creates a dictionary to hold the items for each cluster
        clusters[centroid] = []
    for point in data:  # loops through all data points and assigns them to the correct cluster
        clusters[find_nearest_centroid(centroids, point)].append(point)
    new_centroids = []
    for centroid in clusters.keys():
        # This line may need to change depending on what data is
        mean = [0] * len(data[0])               # creates a list of 0s that is as long as the length of each data point
        for point in clusters[centroid]:        # for each data point in the cluster,
            for i in range(0, len(data[0])):    # add each dimension to the mean
                mean[i] += point[i]
        for i in range(0, len(mean)):           # divide total dimensions by total points in cluster
            mean[i] /= len(clusters[centroid])
        new_centroids.append(mean)              # add the mean to the new_centroids
    is_same_centroids = True                       # a boolean if the centroids are the same
    for centroid in centroids:
        if centroid in new_centroids:           # if the centroid is part of the new centroids,
            pass                                # then don't change anything
        else:                                   # if the centroid is not part of the new centroids,
            is_same_centroids = False              # then the centroids are not the same
    return new_centroids, is_same_centroids, clusters

