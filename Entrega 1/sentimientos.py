import numpy as np
import re

file_path = "./Entrega 1/frases.txt"
feelings_dictionary = {
    'dolor': -1,
    'oscura': -1,
    'perdida': -1,
    'doliente': -1,
    'eterno': 0,
    'amor': 1,
    'fuerte': 1,
    'paz': 1,
    'miseria': -1,
    'esperanza': 1,
    'feliz': 1,
    'caida': -1,
    'oscuridad': -1,
    'luz': 1,
    'gloria': 1,
    'mueve': 1,
    'resplandece': 1,
    'troya': -1,
    'muerta': -1,
    'final': 0,
    'via': 0,
    'odio': -1,
    'paz': 1,
    'victoria': 1
}


def get_phrases(path):
    phrases = []
    with open(path, "r") as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.strip().lower())
            cleaned_phrase = ' '.join(words)
            phrases.append(cleaned_phrase)
    return phrases


def calculate_vectors(frase, key_words, clasificacion):
    w = np.array([1 if word in frase else 0 for word in key_words])
    s = np.array([
        sum([1 for word in key_words if word in frase and clasificacion[word] == 1]),
        sum([1 for word in key_words if word in frase and clasificacion[word] == 0]),
        sum([1 for word in key_words if word in frase and clasificacion[word] == -1])
    ])
    return w, s


def calculate_feeling_quality(w, s, total_key_words):
    average_quality = np.sum(w) / total_key_words
    average_feeling = np.dot([1, 0, -1], s)
    return average_quality, average_feeling

        
phrases = get_phrases(file_path)
selected_words = list(feelings_dictionary.keys())
total_key_words = len(feelings_dictionary)

for i, phrase in enumerate(phrases):
    w, s = calculate_vectors(phrase, selected_words, feelings_dictionary)
    average_quality, average_feeling = calculate_feeling_quality(w, s, total_key_words)
    
    print(f"Frase {i+1}: {phrase}")
    print(f"Vector w: {w}")
    print(f"Vector s: {s}")
    print(f"Calidad Promedio: {average_quality:.2f}")
    print(f"Promedio de Sentimiento: {average_feeling:.2f}")
    print("------")

