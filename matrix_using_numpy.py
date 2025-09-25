import numpy as np

#Creating matrix
arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9,10,11,12],
                 [13,14,15,16]])
print("After creating the array:\n", arr1)

#Adding element
arr2 = np.append(arr1, [[17,18,19,20]], 0)
print("After adding a new row:\n", arr2)
""" 
'0': This specifies the axis along which the new data will be appended. 
In this case, 0 means along the rows (vertically).
"""

#Delete Element
arr2 = np.delete(arr2, [1], 1)
print("After deleting the last column:\n", arr2)