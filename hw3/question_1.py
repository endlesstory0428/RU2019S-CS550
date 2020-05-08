import numpy as np

def getQ(A, X):
	m = np.sum(A) / 2
	k = np.sum(A, axis = 0)

	B = np.empty_like(A, dtype = np.float64)
	for i in range(B.shape[0]):
		for j in range(B.shape[1]):
			B[i, j] = A[i, j] - ((k[i] * k[j]) / (2 * m))
	print(k)

	Q = np.matmul(np.matmul(X, B), X.transpose()) / (4 * m)
	return Q

def Qa1():
	#				 a  b  c  d  e  f  g  h
	A = np.array([	[0, 1, 1, 1, 0, 0, 0, 0], #a
					[1, 0, 1, 1, 0, 0, 0, 0], #b
					[1, 1, 0, 1, 0, 0, 0, 0], #c
					[1, 1, 1, 0, 0, 0, 0, 0], #d
					[0, 0, 0, 0, 0, 1, 1, 0], #e
					[0, 0, 0, 0, 1, 0, 1, 0], #f
					[0, 0, 0, 0, 1, 1, 0, 1], #g
					[0, 0, 0, 0, 0, 0, 1, 0]])#h

	X = np.array([[1, 1, 1, 1, -1, -1, -1, -1]])
	print('A:')
	print(A)
	print('Q:')
	print(getQ(A, X))

def Qa2():
	#				 a  b  c  d  e  f  g  h
	A = np.array([	[0, 1, 1, 1, 0, 0, 1, 0], #a
					[1, 0, 1, 1, 0, 0, 0, 0], #b
					[1, 1, 0, 1, 0, 0, 0, 0], #c
					[1, 1, 1, 0, 0, 0, 0, 0], #d
					[0, 0, 0, 0, 0, 1, 1, 0], #e
					[0, 0, 0, 0, 1, 0, 1, 0], #f
					[1, 0, 0, 0, 1, 1, 0, 1], #g
					[0, 0, 0, 0, 0, 0, 1, 0]])#h

	X = np.array([[1, 1, 1, 1, -1, -1, -1, -1]])
	print('A:')
	print(A)
	print('Q:')
	print(getQ(A, X))

def Qb():
	#				 a  b  c  d  e  f  g  h
	A = np.array([	[0, 1, 1, 1, 0, 0, 1, 0], #a
					[1, 0, 1, 1, 0, 0, 0, 0], #b
					[1, 1, 0, 1, 0, 0, 0, 0], #c
					[1, 1, 1, 0, 0, 0, 0, 0], #d
					[0, 0, 0, 0, 0, 1, 1, 1], #e
					[0, 0, 0, 0, 1, 0, 1, 0], #f
					[1, 0, 0, 0, 1, 1, 0, 1], #g
					[0, 0, 0, 0, 1, 0, 1, 0]])#h

	X = np.array([[1, 1, 1, 1, -1, -1, -1, -1]])
	print('A:')
	print(A)
	print('Q:')
	print(getQ(A, X))

def Qc():
	#				 a  b  c  d  e  f  g  h
	A = np.array([	[0, 1, 1, 1, 0, 1, 1, 0], #a
					[1, 0, 1, 1, 0, 0, 0, 0], #b
					[1, 1, 0, 1, 0, 0, 0, 0], #c
					[1, 1, 1, 0, 0, 0, 0, 0], #d
					[0, 0, 0, 0, 0, 1, 1, 0], #e
					[1, 0, 0, 0, 1, 0, 1, 0], #f
					[1, 0, 0, 0, 1, 1, 0, 1], #g
					[0, 0, 0, 0, 0, 0, 1, 0]])#h

	X = np.array([[1, 1, 1, 1, -1, -1, -1, -1]])
	print('A:')
	print(A)
	print('Q:')
	print(getQ(A, X))

if __name__ == '__main__':
	Qa1()