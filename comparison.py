import numpy as np

#Comparison Operator
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

#True or False
# print(array1 < array2)
# print(array1 > array2)
# print(array1 == array2)
# print(array1 != array2)
# print(array1 >= array2)
# print(array1 <= array2)

scores = np.array([100,80,63,59,50])

scores[scores < 60] = 0

print(scores)