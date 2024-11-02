import numpy as np

# Construye la matriz A que representa las relaciones de luces adyacentes en el tablero.
def construct_matrix_a(n):
    size = n * n
    a_matrix = np.zeros((size, size), dtype=int)
    
    for i in range(n):
        for j in range(n):
            idx = i * n + j
            a_matrix[idx, idx] = 1  # Luz presionada
            # Luz arriba
            if i > 0:
                a_matrix[idx, (i - 1) * n + j] = 1
            # Luz abajo
            if i < n - 1:
                a_matrix[idx, (i + 1) * n + j] = 1
            # Luz a la izquierda
            if j > 0:
                a_matrix[idx, i * n + (j - 1)] = 1
            # Luz a la derecha
            if j < n - 1:
                a_matrix[idx, i * n + (j + 1)] = 1
    
    return a_matrix

# Aplica eliminación gaussiana en módulo 2 sin pivoteo.
def gaussian_elimination_mod2_custom(a_matrix, b_vector):
    size = len(b_vector)

    for i in range(size):
        # Si estamos en un 0, buscaremos hacia abajo un 1 para sumar
        if a_matrix[i, i] == 0:
            found = False
            for j in range(i + 1, size):
                if a_matrix[j, i] == 1:
                    a_matrix[i] = (a_matrix[i] + a_matrix[j]) % 2
                    b_vector[i] = (b_vector[i] + b_vector[j]) % 2
                    found = True
                    break
            
            if not found:  # Si no encontramos un 1, continuar
                continue
        
        # Proceder con eliminación gaussiana
        for j in range(i + 1, size):
            if a_matrix[j, i] == 1:  # Solo si hay un 1 en la posición (j, i)
                a_matrix[j] = (a_matrix[j] + a_matrix[i]) % 2
                b_vector[j] = (b_vector[j] + b_vector[i]) % 2

    # Sustitución hacia atrás para obtener la solución
    for i in range(size - 1, -1, -1):
        if a_matrix[i, i] == 1:
            for j in range(i):
                if a_matrix[j, i] == 1:
                    b_vector[j] = (b_vector[j] + b_vector[i]) % 2

    return b_vector

# Resuelve el juego Lights Out dado una matriz de estado inicial n x n.
def lights_out_solver(board_matrix):
    n = board_matrix.shape[0]
    a_matrix = construct_matrix_a(n)
    b_vector = board_matrix.flatten()
    
    solution_vector = gaussian_elimination_mod2_custom(a_matrix.copy(), b_vector.copy())
    
    return solution_vector

# Aplica la solución y verifica si todas las luces están apagadas.
def apply_solution(board_matrix, pressure_vector):
    n = board_matrix.shape[0]
    new_board = np.copy(board_matrix)

    for i in range(n):
        for j in range(n):
            if pressure_vector[i * n + j] == 1:
                # Presiona la luz (i, j)
                new_board[i, j] = (new_board[i, j] + 1) % 2  # Luz actual
                # Presiona las luces adyacentes
                if i > 0:  # Luz arriba
                    new_board[i - 1, j] = (new_board[i - 1, j] + 1) % 2
                if i < n - 1:  # Luz abajo
                    new_board[i + 1, j] = (new_board[i + 1, j] + 1) % 2
                if j > 0:  # Luz a la izquierda
                    new_board[i, j - 1] = (new_board[i, j - 1] + 1) % 2
                if j < n - 1:  # Luz a la derecha
                    new_board[i, j + 1] = (new_board[i, j + 1] + 1) % 2
    
    return new_board

# Devuelve True si todas las luces están apagadas
def check_solution(board_matrix, pressure_vector):
    final_board = apply_solution(board_matrix, pressure_vector)
    return np.all(final_board == 0)  

# Ejemplo de uso con impresión de resultados
def main():
    try:
        n = int(input("Introduce el tamaño del tablero (n para un tablero n x n): "))
        board_matrix = np.array([
            list(map(int, 
                     input(f"Introduce los valores de la fila {i + 1}, separados por espacios (0 o 1): ").split()))
            for i in range(n)
        ])
        
        print("\nTablero inicial:")
        print(board_matrix)
        
        solution_vector = lights_out_solver(board_matrix)
        
        print("\nSolución (vector de presiones):")
        print(solution_vector)
        print("\nSolución (matriz de presiones):")
        print(solution_vector.reshape((n, n)))

        # Comprobar si la solución apaga todas las luces
        if check_solution(board_matrix, solution_vector):
            print("\nLa solución es válida y apaga todas las luces.")
        else:
            print("\nLa solución no apaga todas las luces.")
            
    except ValueError as e:
        print("Entrada inválida:", e)

if __name__ == "__main__":
    main()
