import numpy as np


def full(N):
    m = np.zeros((N, N))
    for i in range(N):
        m[i] = [int(var) for var in input().split()]
    return m


class Matrix(object):

    def __init__(self, n):
        self.N = n
        self.data = []
        self.indexes = []
        self.indptr = [1]
        self.LU = np.zeros((n, n))

    def csr_matrix_in(self, matrix):
        for i in range(self.N):
            amount = 0
            for j in range(self.N):

                if matrix[i][j] != 0:
                    self.data.append(matrix[i][j])
                    self.indexes.append(j)
                    amount += 1
            self.indptr.append(amount + self.indptr[-1])

    def get_L(self):
        L = self.LU.copy()
        for i in range(L.shape[0]):
            L[i, i] = 1
            L[i, i + 1:] = 0
        return np.matrix(L)

    def get_U(self):
        U = self.LU.copy()
        for i in range(1, U.shape[0]):
            U[i, :i] = 0
        return U

    def decompose_to_LU(self):
        n = self.N

        lu_matrix = np.zeros((n, n))

        for k in range(n):
            # calculate all residual k-row elements
            for j in range(k, n):

                if k > 0:
                    lu_matrix[k, j] = self.get_ij(k, j) - lu_matrix[k, : k] * lu_matrix[: k, j]
                else:
                    lu_matrix[k, j] = self.get_ij(k, j) - lu_matrix[k,k] * lu_matrix[k, j]

            # calculate all residual k-column elemetns
            for i in range(k + 1, n):
                if k > 0:
                    lu_matrix[i, k] = (self.get_ij(i, k) - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]
                else:
                    lu_matrix[i, k] = (self.get_ij(i, k) - lu_matrix[i,k] * lu_matrix[k, k]) / lu_matrix[k, k]
        self.LU = lu_matrix

    def get_ij(self, index_i, index_j):

        for i in range(1, len(self.indptr)):
            for j in range(self.indptr[i] - self.indptr[i - 1]):

                for k in range(self.indexes[self.indptr[i - 1] - 1 + j - 1] + 1
                               if self.indptr[i - 1] - 1 + j - 1 >= 0
                               else 0,
                               self.indexes[self.indptr[i - 1] - 1 + j]):
                    if i == index_i and k == index_j: #Поправить k == index-j
                        return 0

                if i == index_i and self.indexes[self.indptr[i - 1] - 1 + j] == index_j:
                    return int(self.data[self.indptr[i - 1] - 1 + j])

    def csr_matrix_out(self):

        for i in range(1, len(self.indptr)):
            for j in range(self.indptr[i] - self.indptr[i - 1]):

                for k in range(self.indexes[self.indptr[i - 1] - 1 + j - 1] + 1
                               if self.indptr[i - 1] - 1 + j - 1 >= 0
                               else 0,
                               self.indexes[self.indptr[i - 1] - 1 + j]):
                    print(0, "", end='')

                print(int(self.data[self.indptr[i - 1] - 1 + j]), "", end='')
            print()


a = Matrix(4)
matrix = full(4)
a.csr_matrix_in(matrix)
a.decompose_to_LU()
print(a.get_L()*a.get_U())