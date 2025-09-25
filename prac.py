

set1=set([1,2,3,4,5])
set2=set([4,5,6,7,8,1])

uni_set=set1 | set2
print("Union of set1 and set2 is:", type(uni_set), uni_set)

inter_set=set1 & set2
print("Intersection of set1 and set2 is:", type(inter_set), inter_set)

min_set=set1 - set2
print("Elements in set1 but not in set2 is:", type(min_set), min_set)

##
btarray=bytearray((32, 20, 21, 22, 24))
print("Creating Bytearray:")
print(btarray)