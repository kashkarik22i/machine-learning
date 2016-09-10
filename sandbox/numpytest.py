import numpy as np
import scipy as sp

print(np.__version__)

a = np.array([1, 2, 3, 4])

print(a.shape)
print(a.ndim)

b = np.array([[1, 2], [3, 4]])

print(b.shape)
print(b.ndim)

c = b.reshape(4, 1)

b[1][1] = 55

print(b)
print(c)
print(b * 2)
print(a[np.array([1, 2])])
print(a[a < 3])

e = np.array([1, 2, 3, np.NaN, 5])
print(np.mean(e[~np.isnan(e)]))

print(e.dtype)
print(a.dtype)
print(b.dtype)


print(sp.__version__)

print(sp.dot is np.dot)
