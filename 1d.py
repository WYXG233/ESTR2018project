import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

n = 100
for j in range(5):
    x = []
    result_ = np.empty(0)
    count = times = 0
    x_ = np.random.randint(0, 2, size = n)
    for integer in x_:
        x.append(times)
        result_ = np.append(result_, count)
        plt.plot(x, result_, label = 'time ' + str(j+1))
        plt.pause(0.001)
        times += 1
        count += (integer * 2 - 1)
        plt.xlabel('time')
        plt.ylabel('coordinate')
        plt.title('1 dimentional random walk for 100 * 5 times')
plt.show()