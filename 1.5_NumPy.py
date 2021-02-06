import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[3,0],[0,6]])
#print(A+B)
#print(A*2)

X = np.array([[1,2],[3,4],[3,4]])
#print(X)



X = X.flatten()
print(X)

print(X[np.array([0,2,4])])

print(X[X>2])