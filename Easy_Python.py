# Numpy In Python

import Numpy as np # Import the numpy to use numpy features

# 1. Array Creation 

arr1 = np.array([1, 2, 3, 4, 5, 6]) # 1D Array

arr2 = np.array([   
  [1, 2, 3],
  [4, 5, 6]
])  # 2D Array 

# ARRAY INFORMATION

print("Array Shape : ", arr.shape)
print("Dimentions : ", arr.ndim)
print("Size : ", arr.size)
print("Data Types : ", arr.dtypes)

# 3. Special Array 

zeros = np.zeros((2, 3))
print(zeros)

ones = np.ones((2, 2))
print(ones)

identity = np.eye(3)
print(identity)

