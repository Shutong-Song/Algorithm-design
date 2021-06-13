

def mat_chain(dim):
    """
    n is the number of matrices, dim is the number of rows of each matrix in order, the last matrix has both row and column in dim
    for example: A1 (5x2), A2(2x3), A3(3x4), A4(4x6), A5(6x7), A6(7x8), so dim = [5, 2, 3, 4, 6, 7, 8] for A1*A2*...*A6
    input: one dimensional list contains rows of matrices with last matrix (row, col)
    output: the optimal multiplications for A1*...*An, and a list of path to construct the optimal path for multiplication
    dynamic programming with time complexity: O(n^3), space complexity O(n^2)
    """
    n = len(dim) - 1
    M = [[float("inf")]*n for _ in range(n)]
    P = [[0]*n for _ in range(n)]
    for i in range(n):
        M[i][i] = 0
    for diag in range(n): #start from diagonal
        for i in range(n - diag): # row
            j = i + diag
            for k in range(i,j):
                if M[i][j] > M[i][k] + M[k+1][j] + dim[i]*dim[k+1]*dim[j+1]:
                    M[i][j] = M[i][k] + M[k+1][j] + dim[i]*dim[k+1]*dim[j+1]
                    P[i][j] = k
    return M[0][n - 1], P

def print_optimal(P, i, j, res):
    """
    rescontruct the path from Ai*...*Aj
    time complexity: O(j - i)
    """
    if i == j:
        res.append('A' + str(i+1))
    else:
        k = P[i][j]
        res.append("(")
        print_optimal(P, i, k, res)
        print_optimal(P, k+1, j, res)
        res.append(")")
                
if __name__ == "__main__":
    dim = [5, 2, 3, 4, 6, 7, 8]
    dim = [30, 35, 15, 5, 10, 20, 25]
    res, path = mat_chain(dim)
    print(res)
    path_str = []
    print_optimal(path, 0, len(dim) - 2, path_str)
    print("".join(path_str))