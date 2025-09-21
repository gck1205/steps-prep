import pandas as pd
file_path=r"C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\apple_products.csv"

df=pd.read_csv(file_path)
df.head()

df.count()
#
# print(df['Mrp'].min())
print(df['Product Name'][0].upper())
#Sort values

print(df.sort_values(by=['Star Rating'],ascending=False))

# .append: add element to end of list
# .insert: insert element at given index
# .extend: extend one list with another list

lst=[1,2,3,4,5]
lst.insert(2,-10)
print(lst)