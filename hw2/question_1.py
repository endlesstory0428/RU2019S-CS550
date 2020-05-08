import numpy as np

def Qa():
	M = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
	print('M:')
	print(M)
	print('')

	U, s, Vh = np.linalg.svd(M, full_matrices = False)
	print('U:')
	print(U)
	print('Sigma:')
	print(s)
	print('V^T:')
	print(Vh)
	print('')
	return (s, Vh)


def Qb():
	M = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])
	MTM = np.matmul(np.transpose(M), M)

	w, v = np.linalg.eigh(MTM)
	print('Evals:')
	print(w[::-1])
	print('Evces:')
	print(v[::-1])
	print('')
	return (w[::-1], v[::-1])

def Qc(Vh, v):
	print('V:')
	print(np.transpose(Vh))
	print('Evces')
	print(v)
	return

def Qd(s, w):
	print('Sigma^2:')
	print(np.square(s))
	print('Evals:')
	print(w)
	return

if __name__ == '__main__':
	s, Vh = Qa()
	w, v = Qb()
	Qc(Vh, v)
	print('')
	Qd(s, w)