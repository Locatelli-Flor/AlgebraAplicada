from collections import Counter


# Diccionario de letras a números
alphabet = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
    'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26, ' ': 27, '*': 28
}
# Diccionario inverso
alphabet_reverse = {v: k for k, v in alphabet.items()}

# Función para limpiar texto y convertir a mayúsculas
def clean_text(text):
    return ''.join(char for char in text.upper() if char in alphabet)


# Función para cifrar el texto
def encrypt(text, a, b):
    text = clean_text(text)  # Elimina caracteres no permitidos
    encrypted_text = []
    for char in text:
        x = alphabet[char]  # Convertir carácter a número
        encrypted_num = (a * x + b) % 29
        encrypted_text.append(alphabet_reverse[encrypted_num])
    return ''.join(encrypted_text)


# Función para encontrar el inverso modular de a en mod 29
def modular_inverse(a, mod=29):
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    return None  # No hay inverso si esto ocurre


# Función para descifrar el texto
def decrypt(encrypted_text, a, b):
    a_inv = modular_inverse(a)
    if a_inv is None:
        raise ValueError("El inverso modular no existe, elija otro 'a'")
    
    decrypted_text = []
    for char in encrypted_text:
        y = alphabet[char]  # Convertir carácter a número
        decrypted_num = (a_inv * (y - b)) % 29
        decrypted_text.append(alphabet_reverse[decrypted_num])
    return ''.join(decrypted_text)


# Función para contar frecuencias y posiciones
def letter_frequency(text):
    freq = Counter(text)
    positions = {char: [i for i, letter in enumerate(text) if letter == char] for char in freq}
    return freq, positions

# Ejemplo de ejecución
text = """Es por mi que se va a la ciudad del llanto, es por mi que se va al dolor eterno y al lugar 
donde sufre la raza condenada, yo fui creado por el poder divino, la suprema sabiduria y el primer 
amor, y no hubo nada que existiera antes que yo, abandona la esperanza si entras aqui"""

a = 7
b = 2

# Cifrar el texto
encrypted_text = encrypt(text, a, b)
print("Texto encriptado:", encrypted_text)

# Desencriptar el texto
decrypted_text = decrypt(encrypted_text, a, b)
print("Texto desencriptado:", decrypted_text)

# Análisis en el texto original y encriptado
original_freq, original_positions = letter_frequency(text)
encrypted_freq, encrypted_positions = letter_frequency(encrypted_text)

print("Frecuencia y posiciones en el texto original:", original_freq, original_positions)
print("Frecuencia y posiciones en el texto encriptado:", encrypted_freq, encrypted_positions)