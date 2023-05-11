print("===========  Program-25 ============")

print("Using Panada Series")

import pandas as pd

panda_series= pd.Series(["marray", "had", "a", "little", "lamb"])
modified_series= panda_series.map(lambda x: x.capitalize())
print(modified_series)

# Solve same question using list

print("Using List")
list1= ["marray", "had", "a", "little", "lamb"]
modified_list= [item.capitalize() for item in list1]
print(modified_list)




