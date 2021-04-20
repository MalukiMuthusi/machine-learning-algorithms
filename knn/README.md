# K-Nearest Neighbor

It is used to classify data points. It uses a simple classification method
data points closer to each other have shared characteristics.

## The algorithm

```python
# 1. select the number of neighbors you want to use, K
# 2. given a new data point, N, determine it's class.
# 3. calculate the distance from N for each data point.
# 4. sort the data points based on their distance from N.
# 5. select up to K data points from the sorted data points
# 6. find the majority data label, P, of the sorted data points.
# 7. data point N has this label, P.
# 8. terminate.

```

## KNN algorithm for qualitative data

It used to smoothen or predict a new data point.
