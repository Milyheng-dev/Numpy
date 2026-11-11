import numpy as np

#Aggregate functions = summarize data and typically return a single value

array1 = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

# print(np.sum(array1))
# print(np.mean(array1)) #average
# print(np.std(array1)) #standard deviation
print(np.var(array1)) #variant
print(np.min(array1))
print(np.max(array1))
print(np.argmax(array1)) #return index of max number
print(np.argmin(array1))
print(np.sum(array1,axis=0))

# student_A = np.array([48, 49, 50, 51, 52])
# student_B = np.array([10, 30, 50, 70, 90])

# print(np.mean(student_A))
# print(np.std(student_B))

# print("Student A:", np.std(student_A))
# print("Student B:", np.std(student_B))
