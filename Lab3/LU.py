import numpy as np
import random


def full(N):
    m = np.zeros((N, N))
    for i in range(N):
        m[i] = [int(var) for var in input().split()]
    return m


def full_pt_3(N):
    m = [[random.randint(-4, 0) for i in range(N)] for j in range(N)]
    for i in range(N):
        m[i][i] = -sum(m[i][:i] + m[i][i + 1:])
    return np.array(m)


def full_Gilbert(N):
    matrix = np.zeros([N, N])

    for i in range(N):
        for j in range(N):
            matrix[i][j] = 1 / ((i + 1) + (j + 1) - 1)
    return matrix


class Matrix(object):

    def __init__(self, n):
        self.N = n
        self.data = []
        self.indexes = []
        self.indptr = [1]
        self.LU = np.zeros([n, n])
        self.X = np.zeros([n, 1])

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

    def erRate(self, X_new):
        for i in range(self.N):
            self.X[i] = self.X[i] - X_new[i]
        return np.linalg.norm(self.X)

    def numRate(self, A):
        return np.linalg.norm(A)*np.linalg.norm(self.get_inversed())

    def getF(self, matrix):
        for i in range(self.N):
            self.X[i, 0] = i + 1
        return np.dot(matrix, self.X)

    def get_U(self):
        U = self.LU.copy()
        for i in range(1, U.shape[0]):
            U[i, :i] = 0
        return U

    def decompose_to_LU(self):
        n = self.N

        lu_matrix = np.zeros([n, n])

        for k in range(n):

            # calculate all residual k-row elements
            for j in range(k, n):
                if k > 0:
                    lu_matrix[k, j] = float(self.get_ij(k, j) - np.dot(lu_matrix[k, : k], lu_matrix[: k, j]))
                else:
                    lu_matrix[k, j] = float(self.get_ij(k, j) - lu_matrix[k, k] * lu_matrix[k, j])

            # check if matrix is degenerate
            if float(lu_matrix[k, k]) == 0:
                return -1

            # calculate all residual k-column elemetns
            for i in range(k + 1, n):
                if k > 0:
                    lu_matrix[i, k] = (self.get_ij(i, k) - np.dot(lu_matrix[i, : k], lu_matrix[: k, k])) / lu_matrix[
                        k, k]
                else:
                    lu_matrix[i, k] = (self.get_ij(i, k) - lu_matrix[i, k] * lu_matrix[k, k]) / lu_matrix[k, k]

        self.LU = lu_matrix

        return 0

    def solve_LU(self, b):

        # get supporting vector y
        y = np.zeros([self.LU.shape[0], 1])

        for i in range(y.shape[0]):
            y[i, 0] = b[i, 0] - np.dot(self.LU[i, :i], y[:i])

        # get vector of answers x
        x = np.zeros([self.LU.shape[0], 1])

        for i in range(1, x.shape[0] + 1):
            x[-i, 0] = (y[-i] - np.dot(self.LU[-i, -i:], x[-i:, 0])) / self.LU[-i, -i]

        return x

    def get_inversed(self):
        inversed = None
        for i in range(self.LU.shape[0]):
            b = np.zeros([self.LU.shape[0], 1])
            b[i, 0] = 1
            column = self.solve_LU(b)
            if inversed is None:
                inversed = column
            else:
                inversed = np.append(inversed, column, axis=1)
        return inversed

    def get_ij(self, index_i, index_j):
        answer = 0
        row_length = self.indptr[index_i + 1] - self.indptr[index_i]
        first_row_index = self.indptr[index_i] - 1
        last_row_index = self.indptr[index_i] - 1 + row_length
        for k in range(first_row_index, last_row_index):
            if self.indexes[k] == index_j:
                answer = self.data[k]
        return answer

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
flag = a.decompose_to_LU()
if flag == -1:
    print("This matrix is degenerate.")
else:
    print(a.get_L())
    print(a.get_U())
    print(a.get_L() * a.get_U())
    inversed = a.get_inversed()
    print(inversed)
    print(matrix.dot(inversed))

# matrix_pt_3 = full_pt_3(4)
# print(matrix_pt_3)

a_gilbert = Matrix(10)
matrix_gilbert = full_Gilbert(10)
a_gilbert.csr_matrix_in(matrix_gilbert)
flag = a_gilbert.decompose_to_LU()
if flag == -1:
    print("This matrix is degenerate.")
else:
    F = a_gilbert.getF(matrix_gilbert)
    X_new = a_gilbert.solve_LU(F)
    print(a_gilbert.erRate(X_new))
    print(a_gilbert.numRate(matrix_gilbert))
