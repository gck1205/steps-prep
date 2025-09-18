import os
import datetime
import pandas as pd
# import pyspark
# from pyspark.sql import SparkSession

# print(datetime.datetime.now())

lst = [("Chaitanya",11),("Revansh",12),("Rushanka",13)]

df=pd.DataFrame(lst,columns=["Name","Id"])
print(df.head())
