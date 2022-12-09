import numpy as np
import matplotlib.pyplot as plt

n = 10000
T = 100
mu, sigma = 0, n ** 0.5
result_ = np.empty(0)
fig = plt.subplots(figsize = (11,5))
for j in range(T):
    e_ = np.empty(0)
    for i in range(n):
        count = 0
        x_ = np.random.randint(0, 2, size = n)
        for integer in x_:
            count += (integer * 2 - 1)
        e_ = np.append(e_,count ** 2)
    t = np.sum(e_)
    t /= n
    t = int(t)
    result_ = np.append(result_, t)
    #print(str(j) + 'done')
plt.scatter(range(1,T+1),result_,label = 'E(d2)')
plt.axhline(y=n, color='r', linestyle='--',label = 'y = n')
plt.legend('best')
plt.show()