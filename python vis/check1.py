import seaborn as sns

 
sns.countplot(x='gender',data=ds)

print(ds.gender.value_counts())
 
sns.countplot(x='gender',hue='smoker',data=ds)

print(ds.gender.value_counts())