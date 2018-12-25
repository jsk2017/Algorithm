import numpy as np

a = np.array([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
b = np.array([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])
c = a+b

#如果c是可逆矩阵，那么

d = np.mat(c)
re_matrix = d.I