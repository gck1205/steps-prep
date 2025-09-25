#Creating list
numbers = [1, 2, 3, 4, 5]
name = ["Shayan", "Shohan", "Dola", "Mona", "Moni"]
#Creating a multidimensional list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

#Access element of list using index
print("Accessing the middle element of the matrix:", matrix[1][1])
#Access element of list using negative index
print("Last element of the name list is:",name[-1])

#Insert a element to a position[list_name.insert(position, value)]
numbers.insert(0, 0)
print("numbers list after insertion:", numbers)
#Appending a element to the list
numbers.append(6)
print("Elements of numbers list after appending:", numbers)

#Remove a number from the list
numbers.remove(0)
print("Elements of number list after removing the first element:", numbers)
#Pop the last element from the list
numbers.pop()
print("Elements of numbers list after popping the last element:", numbers)

#Reverse the list
numbers.reverse()
print("Elements of numbers list after reversing:", numbers)
#Sort the list
name.sort()
print("Name list after being sorted:", name)