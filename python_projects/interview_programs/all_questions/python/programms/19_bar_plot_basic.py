print("question 18")


# importing the required module
import matplotlib.pyplot as plt

# creating the dataset
data = {'apple':20, 'banana':15, 'orange':30,'grapes':35}

fruits = list(data.keys())
costs = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(fruits, costs, color ='blue', width = 0.4)

# naming the x axis
plt.xlabel('Fruits')
# naming the y axis
plt.ylabel('Costs')

# giving a title to my graph
plt.title('Fruit vs Cost')

# function to show the plot
plt.show()


