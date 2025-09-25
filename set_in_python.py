"""
Set in python is a mutable collection of data that does not allow any duplication.
The data structure used in this is Hashing, a popular technique to perform insertion, 
deletion, and traversal in O(1) on average.
"""
# Create Set
Male_names = set(["Shayan", "Shohan", "Shopnil", "Mugdho", "Efty"])
Female_names = set(["Hamima", "Pushon", "Dristy", "Efty", "Shopnil", "Safa", "Megha"])

#Add element to set
Male_names.add("Megh")
#Remove element from set
Female_names.remove("Megha")

#intersection in set
common_names = Male_names & Female_names
print("Common Names:", common_names)
#Union in set
all_names = Male_names | Female_names
print("All names:", all_names)
#Subtraction in set
uncommon_names = all_names - common_names
print("Uncommon names:", uncommon_names)

#Access elements using for loop
for name in all_names:
    print(name, end=" ")