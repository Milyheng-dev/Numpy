import numpy as np

# print(np.__version__)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# normal python
# my_list = my_list * 2

# array = np.array(my_list) * 2

#0 dimension
dimension0 = np.array(['A'])

#1 dimension
dimension1 = np.array(['A','B','C'])

#2 dimension
dimension2 = np.array([['A', 'B', 'C'],
                       ['A', 'B', 'C']])

#3 dimension
dimension3 = np.array([[['A', 'B', 'C'], ['A', 'B', 'C']],
                       [['A', 'B', 'C'], ['A', 'B', 'C']]])



#it will show an error because it needs sequent
# dimension3 = np.array([[['A', 'B', 'C'], ['A', 'B', 'C']],
#                        [['A', 'B', 'C'], ['A', 'B']]])

#shape
# print(dimension3.shape)

#to access index
# print(dimension3[0][0][0])

#multidimensional indexing
# print(dimension3[0 ,0 , 2])
# print(dimension3[0 , 0])
# print(dimension3[0 ])


#string Concatenation [layer,row,column]
word = dimension3[0 ,0 ,0] + dimension3[1 ,1 ,1] + dimension3[1 ,1 ,1]


#slicing
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#access array[start:end:step]

# print(array[0])
# print()
# print(array[0:4])
# print()
# print(array[0:4:2])
# print()
# print(array[:1:1])
# print()
# print(array[::1])


#access row
# print(array[0:2,])

#access column
# print(array[:,1:2])


