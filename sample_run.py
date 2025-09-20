import os
import datetime
import pandas as pd
# import pyspark
# from pyspark.sql import SparkSession

# print(datetime.datetime.now())

lst = [("Chaitanya",11),("Revansh",12),("Rushanka",13)]

df=pd.DataFrame(lst,columns=["Name","Id"])
print(df.head())

#Identify duplicates
#Below is the input
list_with_duplicates = [1,1,1,1,2,2,2,3,3,3,3,4,4,5]

new_set=set(list_with_duplicates)
newlist=list(new_set)
print(newlist)
print(new_set)

#Numbers divisible by 7 and not multiple of 5
result = [x for x in range(1, 150) if (x % 7 == 0 and x%5 != 0)]
print(result)

#print prime numbers between 1-150
prime_list=[]
i,j=0,0
for i in range(2, 150):
    for j in range(2, 150):
        if (i%j == 0):
            break
    if i == j:
        prime_list.append(i)
print(prime_list)

#Write a program to count the number of words in string variable
string1 = "Hello this is an example string with several words this is a test string"
words = string1.split()
num_words = len(words)
print("Number of words in the string:", num_words)

#Print only the string values from the input list
complex_nested_list = ['a','b',['cc','dd',['eee','fff'],'gg'],'hhhh','ii']
flat_list = []
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            flatten(item)
        else:
            flat_list.append(item)
flatten(complex_nested_list)
print(flat_list)  

#Write a Python function to find the largest number in a list
def find_largest_number(input_list):
    if not input_list:
        return None
    largest_number = input_list[0]
    for number in input_list:
        if number > largest_number:
            largest_number = number
    return largest_number
numbers = [3, 5, 7, 2, 8, -1, 4]
largest = find_largest_number(numbers)
print("The largest number in the list is:", largest)

#Write a Python function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

string_to_reverse = "Hello, World!"
reversed_string = reverse_string(string_to_reverse) 
print("Reversed string:", reversed_string)

#Python function to reverse a string without using string slicing
def reverse_string_no_slicing(input_string):
    reversed_str = ''
    for char in input_string:
        print(char + reversed_str)
        reversed_str = char + reversed_str
    return reversed_str

string_to_reverse = "Hello, World123!"
reversed_string = reverse_string_no_slicing(string_to_reverse)      
print("Reversed string without slicing:", reversed_string)


###Create different types of arrays
string_array=[]
integer_array=[]
list_array=[]
boolean_array=[]
float_array=[]
list_with_multiple_dt = [1,"Python",1.10,True,[1,2,3,4],False,False,'AWS','Spark',60.70,555.5,46,['Looping','Conditional Statements',['Test'],100.5],90,True,False,20.6,33,'Google']

for k in list_with_multiple_dt:
    if isinstance(k,list):
       list_array.append(k)
    if isinstance(k,str):
       string_array.append(k)
    if isinstance(k,bool):
       boolean_array.append(k)   
    if isinstance(k,int):
       integer_array.append(k)
    if isinstance(k,float):
       float_array.append(k)
       
print("List Array:",list_array,'\n',string_array,'\n',integer_array,'\n',float_array,'\n',boolean_array)