import random
import numpy as np
import re

file_path = "./Entrega 1/frases.txt"
dict_feelings = {
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
    'sabe': 0
}


def getPhrases(path):
    phrases = []
    with open(path, "r") as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line.strip().lower())
            cleaned_phrase = ' '.join(words)
            phrases.append(cleaned_phrase)
    return phrases


def calcular_vectores(frase, palabras_clave, clasificacion):
    w = np.array([1 if palabra in frase else 0 for palabra in palabras_clave])
    s = np.array([
        sum([1 for palabra in palabras_clave if palabra in frase and clasificacion[palabra] == 1]),
        sum([1 for palabra in palabras_clave if palabra in frase and clasificacion[palabra] == 0]),
        sum([1 for palabra in palabras_clave if palabra in frase and clasificacion[palabra] == -1])
    ])
    return w, s


def calcular_calidad_sentimiento(w, s, total_palabras_clave):
    calidad_promedio = np.sum(w) / total_palabras_clave
    promedio_sentimiento = np.dot([1, 0, -1], s)
    return calidad_promedio, promedio_sentimiento
        
    

phrases = getPhrases(file_path)
random_words = random.sample(list(dict_feelings.keys()), 6)
total_palabras_clave = len(dict_feelings)
print(f"Palabras clave: {random_words}")

for i, frase in enumerate(phrases):
    w, s = calcular_vectores(frase, random_words, dict_feelings)
    calidad_promedio, promedio_sentimiento = calcular_calidad_sentimiento(w, s, total_palabras_clave)
    
    print(f"Frase {i+1}: {frase}")
    print(f"Vector w: {w}")
    print(f"Vector s: {s}")
    print(f"Calidad Promedio: {calidad_promedio:.2f}")
    print(f"Promedio de Sentimiento: {promedio_sentimiento:.2f}")
    print("------")

