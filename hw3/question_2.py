import numpy as np

def Qa():
	#				 a  b  c  d  e  f  g  h
	A = np.array([	[0, 1, 1, 1, 0, 0, 1, 0], #a
					[1, 0, 1, 1, 0, 0, 0, 0], #b
					[1, 1, 0, 1, 0, 0, 0, 0], #c
					[1, 1, 1, 0, 0, 0, 0, 0], #d
					[0, 0, 0, 0, 0, 1, 1, 0], #e
					[0, 0, 0, 0, 1, 0, 1, 0], #f
					[1, 0, 0, 0, 1, 1, 0, 1], #g
					[0, 0, 0, 0, 0, 0, 1, 0]])#h
	print('A:')
	print(A)

	D = np.diag(np.sum(A, axis = 0))
	print('D:')
	print(D)

	L = D - A
	print('L:')
	print(L)
	return L

def Qb(L):
	w, v = np.linalg.eigh(L)
	v = v.transpose()
	print('eigenvalues:')
	print(w)
	print('eigenvectors')
	print(v)
	return v[1]

if __name__ == '__main__':
	L = Qa()
	Qb(L)