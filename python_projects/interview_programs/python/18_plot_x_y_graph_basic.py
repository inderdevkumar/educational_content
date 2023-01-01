print("question 18")


# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [0,1,2,3,4,5,6,7,8,9,10]
# corresponding y axis values
y = [0,1,2,3,4,5,6,7,8,9,10]

# plotting the points 
plt.plot(x, y)

# naming the x axis
plt.xlabel('x-axis')
# naming the y axis
plt.ylabel('y-axis')

# giving a title to my graph
plt.title('Y vs X')

# function to show the plot
plt.show()


