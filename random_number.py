import numpy as np

#integer
# rng = np.random.default_rng(seed = 1)
#
# for i in range(1,3):
#     # print(rng.integers(low = 1, high = 101,size = 3)) #only column
#     print(rng.integers(low=1, high=101, size=[3,2])) #row and column


#float
# np.random.seed(seed=1)
# print(np.random.uniform (low= -1,high= 1, size = 3))

array = np.array([1,2,3,4,5,6])
rng = np.random.default_rng()
rng.shuffle(array)

print(array)