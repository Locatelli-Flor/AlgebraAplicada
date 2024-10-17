import numpy as np


def construct_matrix_A(rows, cols):
    size = rows * cols
    A = np.zeros((size, size), dtype=int)
    
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            A[idx, idx] = 1  # La luz presionada
            if i > 0:
                A[idx, (i-1) * cols + j] = 1  # Luz arriba
            if i < rows-1:
                A[idx, (i+1) * cols + j] = 1  # Luz abajo
            if j > 0:
                A[idx, i * cols + (j-1)] = 1  # Luz a la izquierda
            if j < cols-1:
                A[idx, i * cols + (j+1)] = 1  # Luz a la derecha
    
    return A


def gaussian_elimination_mod2(A, b):
    size = len(b)
    
    # Eliminación gaussiana
    for i in range(size):
        if A[i, i] == 0:
            for j in range(i+1, size):
                if A[j, i] == 1:
                    A[[i, j]] = A[[j, i]]  # Intercambio de filas
                    b[i], b[j] = b[j], b[i]
                    break
        # Hacemos las otras filas 0 en la columna i
        for j in range(size):
            if i != j and A[j, i] == 1:
                A[j] = (A[j] + A[i]) % 2
                b[j] = (b[j] + b[i]) % 2

    return b


def lights_out_solver(board):
    # Validaciones del tablero
    if board is None or len(board) == 0 or len(board[0]) == 0:
        return "No hay tablero o está vacío"
    
    if np.any(board < 0) or np.any(board > 1):
        return "El tablero debe contener solo 0s y 1s"
    

    if len(board) != len(board[0]):
        return "El tablero debe ser cuadrado"
    

    rows, cols = board.shape
    A = construct_matrix_A(rows, cols)
    b = board.flatten()

    solution = gaussian_elimination_mod2(A, b)
    
    return solution


board = np.array([
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0]
])
solution = lights_out_solver(board)
print(solution)
