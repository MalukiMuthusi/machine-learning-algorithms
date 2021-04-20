# KNN Clustering

It is an instance based learning algorithm.
You must know the number if classes in your data before using the algorithm.
The algorithm groups your data into clusters.

## The algorithm

```python
# 1. determine the number of clusters
# 2. create a global matrix that is used to tell a data point is in which cluster
#       at any point.
# 3. at the start the data points are not in any cluster.
# 4. for the clusters k that you picked, pick some data point to act as the initial
#       centroids of your clusters.
# 5. using the centroids calculate the distance of each data point form the centroids.
# 6. the data point can be only in a single cluster.
# 7. place the data point into the cluster in which it is closer to its centroid.
# 8. update the global matrix to show which clusters each data point belongs to currently.
# 9. repeat
#       10. for each cluster calculate its new centroid by finding the mean of the data points.
#       11. calculate the distance of each data point from the centroids.
#       12 place each data point into the cluster in which it is closer to the centroid.
#       13. update the global matrix to show the which clusters the data points belong currently.
#       15. check if the global matrix has changed.
#       16.     if it has not changed the data points are in their right cluster.
# 15. terminate.

```
