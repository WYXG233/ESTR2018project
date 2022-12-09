import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

Color = {
    '0' : 'red',
    '1' : 'blue',
    '2' : 'darkorange',
    '3' : 'black',
    '4' : 'seagreen',
}

n = 100
ax = plt.axes(projection='3d')
for j in range(5):
    x1 = x2 = y1 = y2 = z1 = z2 = 0
    x_ = np.random.randint(0, 6, size = n)
    ax.scatter3D(x1, y1, z1, color = 'black')
    for integer in x_:
        x1 = x2
        y1 = y2
        z1 = z2
        if integer == 0:#up
            y2 += 1
        if integer == 1:#down
            y2 -= 1
        if integer == 2:#left
            x2 -= 1
        if integer == 3:#right
            x2 += 1
        if integer == 4:#front
            z2 -= 1
        if integer == 5:#back
            z2 += 1

        plt.plot([x1,x2], [y1,y2], [z1, z2], color = Color.get(str(j),'red'))
        plt.pause(0.1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('3 dimentional random walk for 100 * 5 times')
    ax.scatter3D(x2, y2, z2, color = Color.get(str(j),'red'))
plt.show()