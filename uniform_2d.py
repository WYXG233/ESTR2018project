import numpy as np
import matplotlib.pyplot as plt

Color = {
    '0' : 'red',
    '1' : 'blue',
    '2' : 'darkorange',
    '3' : 'black',
    '4' : 'seagreen',
}

n = 100
plt.figure(figsize=(8, 6), dpi=80) 
ax = plt.gca()
for j in range(5):
    x1 = x2 = y1 = y2 = 0
    x_ = np.random.uniform(0, 2 * np.pi, size = n)
    plt.scatter(x1, y1, color = 'black')
    for integer in x_:
        x1 = x2
        y1 = y2
        x2 += np.cos(integer)
        y2 += np.sin(integer)
        plt.axis('equal')
        
        plt.plot([x1,x2], [y1,y2], color = Color.get(str(j),'red'))
        plt.pause(0.1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('2 dimentional random walk for 100 * 5 times')
    plt.scatter(x2,y2, color = Color.get(str(j),'red'))
plt.show()