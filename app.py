import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

# 100 linearly spaced numbers

# f(x) = x^3 + 1 
x1 = np.linspace(-5,5,100)
y1 = x1**3 + 1 

# g(x) = 5x -11
x2 = np.linspace(-5,5,100)
y2 = 5*x2 - 11


# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.style.use('seaborn')

plt.title('Math it\'s cool')
plt.ylabel('y axis')
plt.xlabel('x axis')

plt.grid(True, color='g')




# plot the function
plt.plot(x1,y1,'r',linewidth=4, label='f(x)')
# plt.plot(x2,y2,'w',linewidth=4, label='line1')
# plt.plot(x1,y1, 'r')
plt.plot(x2,y2, 'r', linewidth=2, label='g(x)')
ax.legend()

# show the plot
plt.show()