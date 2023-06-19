import pandas as pd

list_1d_data= [1,2,3,4]
list_2d_data= [[1,2,3,4], [5,6,7,8]]

dict_data= {"student": ["x", "y", "z"], "fruit": ["apple", "banana", "orange"]}

dict_normal_data= {"a": "val1", "b": "val2"}


df_list_1d= pd.DataFrame(list_1d_data)
df_list_2d= pd.DataFrame(list_2d_data)
df_list_2d_with_user_columns= pd.DataFrame(list_2d_data, columns=["c1", "c2", "c3", "c4"])

df_dict= pd.DataFrame(dict_data)
df_dict_normal_data= pd.DataFrame(dict_normal_data.items()) # importance of items()


print(df_list_1d)
print(df_list_2d)
print(df_list_2d_with_user_columns)
print(df_dict)
print(df_dict_normal_data)

# Revert back to repective list and dict from datframe

back_to_list_1d= df_list_1d.stack().tolist()  #Important of stack()
back_to_2d_list= df_list_2d.values.tolist()

back_to_dict= df_dict.to_dict('list')
back_to_dict_normal= dict(df_dict_normal_data.values)

print(back_to_list_1d)
print(back_to_2d_list)
print(back_to_dict)
print(back_to_dict_normal)
