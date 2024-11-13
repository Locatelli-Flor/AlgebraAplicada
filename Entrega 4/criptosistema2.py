import numpy as np
from collections import Counter
import re


# Tabla de conversión letras ↔ números
char_to_num = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14,
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 28
}
num_to_char = {v: k for k, v in char_to_num.items()}

# Configuración de T y b
T = np.array([[1, 2, 3], [0, 1, 4], [0, 0, 1]])
b = np.array([1, 2, 3])


# Función para limpiar texto y convertir a bloques de tamaño 3
def clean_text(text):
    # Convertir a mayúsculas y eliminar caracteres no permitidos
    cleaned_text = re.sub(r'[^A-ZÑ ]', '', text.upper())
    # Asegurar que el texto sea múltiplo de 3, agregando espacios si es necesario
    if len(cleaned_text) % 3 != 0:
        cleaned_text += ' ' * (3 - len(cleaned_text) % 3)
    return cleaned_text


# Función para convertir texto a bloques de 3 y luego a vectores
def text_to_vectors(text):
    blocks = [text[i:i+3] for i in range(0, len(text), 3)]
    vectors = [np.array([char_to_num[char] for char in block]) for block in blocks]
    return vectors


# Función de encriptado
def encrypt(text):
    cleaned_text = clean_text(text)
    vectors = text_to_vectors(cleaned_text)
    encrypted_vectors = [(T @ v + b) % 29 for v in vectors]
    encrypted_text = ''.join(''.join(num_to_char[num] for num in vec) for vec in encrypted_vectors)
    return encrypted_text, encrypted_vectors


def decrypt(encrypted_text):
    T_inv = np.linalg.inv(T).astype(int) % 29  # Inversa de T en Z_29
    encrypted_vectors = text_to_vectors(encrypted_text)
    decrypted_vectors = [(T_inv @ (vec - b)) % 29 for vec in encrypted_vectors]
    decrypted_text = ''.join(''.join(num_to_char[num] for num in vec) for vec in decrypted_vectors)
    return decrypted_text, decrypted_vectors


# Función para encontrar el bloque de 3 caracteres más repetido y posiciones
def letter_frequency(vectors):
    # Convertir cada vector en una tupla para poder contar su frecuencia
    vector_tuples = [tuple(int(num) for num in vec) for vec in vectors]
    counter = Counter(vector_tuples)
    most_common = counter.most_common(1)[0]
    most_repeated_block, _ = most_common
    positions = [i for i, vec in enumerate(vector_tuples) if vec == most_repeated_block]
    return most_repeated_block, positions


# Ejemplo de uso
text = """Es por mi que se va a la ciudad del llanto, es por mi que se va al dolor eterno y al lugar 
donde sufre la raza condenada, yo fui creado por el poder divino, la suprema sabiduria y el primer 
amor, y no hubo nada que existiera antes que yo, abandona la esperanza si entras aqui"""

encrypted_text, encrypted_vectors = encrypt(text)
print("Texto encriptado:", encrypted_text, '\n')
decrypted_text, decrypted_vectors = decrypt(encrypted_text)
print("Texto desencriptado:", decrypted_text, '\n')

# Análisis del bloque de 3 caracteres más repetido en los textos encriptado y desencriptado
decrypted_most_repeated_block, decrypted_positions = letter_frequency(decrypted_vectors)
print("Bloque de 3 caracteres más repetido en el desencriptado:", decrypted_most_repeated_block)
print("Posiciones del bloque en el desencriptado:", decrypted_positions)

encrypted_most_repeated_block, encrypted_positions = letter_frequency(encrypted_vectors)
print("Bloque de 3 caracteres más repetido en el encriptado:", encrypted_most_repeated_block)
print("Posiciones del bloque en el encriptado:", encrypted_positions, '\n')