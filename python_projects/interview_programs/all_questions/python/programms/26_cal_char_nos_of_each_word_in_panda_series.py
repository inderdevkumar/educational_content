print(" ========  Program-26========== ")

print("Using panda series")
import pandas as pd

panda_series= pd.Series(["marry", "had", "a", "little", "lamb"])

count_length_series= panda_series.map(lambda x: len(x))
print(count_length_series)


print("Using List")

list1= ["marry", "had", "a", "little", "lamb"]


count_length= [len(item) for item in list1]

print(count_length)

