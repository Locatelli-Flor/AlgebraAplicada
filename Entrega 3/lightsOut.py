import numpy as np


# Construye la matriz A que representa las relaciones de luces adyacentes en el tablero.
def construct_matrix_a(rows, cols):
    size = rows * cols
    a_matrix = np.zeros((size, size), dtype=int)
    
    for i in range(rows):
        for j in range(cols):
            idx = i * cols + j
            a_matrix[idx, idx] = 1  # Luz presionada
            if i > 0:
                a_matrix[idx, (i - 1) * cols + j] = 1  # Luz arriba
            if i < rows - 1:
                a_matrix[idx, (i + 1) * cols + j] = 1  # Luz abajo
            if j > 0:
                a_matrix[idx, i * cols + (j - 1)] = 1  # Luz a la izquierda
            if j < cols - 1:
                a_matrix[idx, i * cols + (j + 1)] = 1  # Luz a la derecha
    
    return a_matrix


# Aplica eliminación gaussiana en módulo 2 para resolver el sistema de ecuaciones.
def gaussian_elimination_mod2(a_matrix, b_vector):
    size = len(b_vector)
    
    for i in range(size):
        if not a_matrix[i, i]:  # Intercambio de filas si el pivote es 0
            for j in range(i + 1, size):
                if a_matrix[j, i]:
                    a_matrix[[i, j]] = a_matrix[[j, i]]
                    b_vector[i], b_vector[j] = b_vector[j], b_vector[i]
                    break
        
        for j in range(size):
            if i != j and a_matrix[j, i] == 1:
                a_matrix[j] = (a_matrix[j] + a_matrix[i]) % 2
                b_vector[j] = (b_vector[j] + b_vector[i]) % 2

    return b_vector


# Resuelve el juego Lights Out dado un vector de estado inicial del tablero.
def lights_out_solver(board_vector, size):
    if len(board_vector) != size * size:
        return "El vector no corresponde al tamaño del tablero especificado."
    
    board = np.array(board_vector).reshape((size, size))
    a_matrix = construct_matrix_a(size, size)
    b_vector = board.flatten()
    solution_vector = gaussian_elimination_mod2(a_matrix, b_vector)
    solution_matrix = solution_vector.reshape((size, size))
    
    return solution_vector, solution_matrix

    
# Imprime el tablero de forma visual.
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print("\n")

# Ejecución interactiva
try:
    size = int(input("Introduce el tamaño del tablero (n para un tablero n x n): "))
    board_vector = list(map(int, input(f"Introduce los {size * size} valores del tablero en una sola línea, separados por espacios: ").split()))
    
    print("\nTablero inicial:")
    print_board(np.array(board_vector).reshape((size, size)))
    
    solution_vector, solution_matrix = lights_out_solver(board_vector, size)
    
    print("Solución (vector de presiones):")
    print(solution_vector)
    print("\nSolución (matriz de presiones):")
    print_board(solution_matrix)

except ValueError:
    print("Entrada inválida. Asegúrate de ingresar solo números enteros.")
