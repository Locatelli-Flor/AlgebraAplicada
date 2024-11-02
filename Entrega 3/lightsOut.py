import numpy as np

def construct_matrix_A(rows, cols):
     # Construye la matriz A que representa las relaciones de luces adyacentes en el tablero.
    size = rows * cols
    A = np.zeros((size, size), dtype=int)
    
    # Configuración de la matriz A de acuerdo a la posición de cada luz y sus adyacentes
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            A[idx, idx] = 1  # Luz presionada
            if i > 0:
                A[idx, (i - 1) * cols + j] = 1  # Luz arriba
            if i < rows - 1:
                A[idx, (i + 1) * cols + j] = 1  # Luz abajo
            if j > 0:
                A[idx, i * cols + (j - 1)] = 1  # Luz a la izquierda
            if j < cols - 1:
                A[idx, i * cols + (j + 1)] = 1  # Luz a la derecha
    
    return A

def gaussian_elimination_mod2(A, b):
    size = len(b)
    
    for i in range(size):
        # Intercambio de filas si el pivote es 0
        if A[i, i] == 0:
            for j in range(i + 1, size):
                if A[j, i] == 1:
                    A[[i, j]] = A[[j, i]]
                    b[i], b[j] = b[j], b[i]
                    break
        
        # Hacer cero los elementos en otras filas de la columna actual
        for j in range(size):
            if i != j and A[j, i] == 1:
                A[j] = (A[j] + A[i]) % 2
                b[j] = (b[j] + b[i]) % 2

    return b

def lights_out_solver(board_vector, size):
    # Resuelve el juego Lights Out dado un vector de estado inicial del tablero.
    if len(board_vector) != size * size:
        return "El vector no corresponde al tamaño del tablero especificado."
    
    board = np.array(board_vector).reshape((size, size))
    
    A = construct_matrix_A(size, size)
    b = board.flatten()
    solution_vector = gaussian_elimination_mod2(A, b)
    solution_matrix = solution_vector.reshape((size, size))
    
    return solution_vector, solution_matrix

def print_board(board):
    # Imprime el tablero de forma visual.
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Ejecución interactiva
try:
    size = int(input("Introduce el tamaño del tablero (n para un tablero n x n): "))
    board_vector = list(map(int, input(f"Introduce los {size*size} valores del tablero en una sola línea, separados por espacios: ").split()))
    
    print("\nTablero inicial:")
    print_board(np.array(board_vector).reshape((size, size)))
    
    solution_vector, solution_matrix = lights_out_solver(board_vector, size)
    
    print("Solución (vector de presiones):")
    print(solution_vector)
    print("\nSolución (matriz de presiones):")
    print_board(solution_matrix)

except ValueError:
    print("Entrada inválida. Asegúrate de ingresar solo números enteros.")
