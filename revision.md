# Revision

- Describe How ID3 algorithm of Decision Tree works.

## ID3 Algorithm

```python
# 1. Establish classification attribute, in table R.
# 2. Compute the classification entropy.
# 3. For each attribute in R, calculate information gain using classification attribute.
# 4. Select attribute with highest gain to be the next node in the tree, starting from the root node.
# 5. Remove node attribute, creating reduced table, Rs.
# 6. Repeat steps 3-5 until all attributes have been used, or the same classification values remain for all the rows in the table.
```

- You can prune the unique attributes from the data.
