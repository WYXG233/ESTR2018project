import numpy as np
import matplotlib.pyplot as plt

n = 10000
mu, sigma = 0, n ** 0.5
result_ = np.empty(0)
for i in range(n):
    count = 0
    x_ = np.random.randint(0, 2, size = n)
    for integer in x_:
        count += (integer * 2 - 1)
    result_ = np.append(result_, count)

n_, bins, patches = plt.hist(result_, 60, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
            np.exp(-1/2 * ((bins - mu)/sigma)**2),
        linewidth=2, color='r')
plt.xlabel('coodinate')
plt.ylabel('probability')
plt.title('10000 times random walk & normal distribution')
plt.show()

n_, bins, patches = plt.hist(result_, 60, cumulative=True,density= True)
plt.xlabel('coodinate')
plt.ylabel('probability')
plt.title('1D CDF')
plt.show()
