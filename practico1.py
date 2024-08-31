import numpy as np

def leer_palabras_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        return {linea.strip() for linea in f}

palabras_positivas = leer_palabras_archivo('positivas.txt')
palabras_neutrales = leer_palabras_archivo('neutrales.txt')
palabras_negativas = leer_palabras_archivo('negativas.txt')

with open('frases.txt', 'r', encoding='utf-8') as f:
    frases = f.readlines()

frases = [frase.strip() for frase in frases]

def calcular_vectores(frase, positivas, neutrales, negativas):
    palabras = set(frase.lower().split())

    todas_palabras = list(positivas | neutrales | negativas)
    w = np.array([
        1 if palabra in palabras else 0
        for palabra in todas_palabras
    ])

    s = np.array([
        np.sum([
            palabra in palabras
            for palabra in positivas
        ]),

        np.sum([
            palabra in palabras
            for palabra in neutrales
        ]),

        np.sum([
            palabra in palabras
            for palabra in negativas
        ])
    ])

    return w, s


def avg(w):
    return np.mean(w)


def producto_escalar(s):
    sentimiento_base = np.array([1, 0, -1])
    return np.dot(sentimiento_base, s)


def promedio_sentimiento(s):
    total = s[0]+s[1]+s[2]
    s0 = float(s[0] / total)
    s1 = float(s[1] / total)
    s2 = float(s[2] / total)
    promedio = [s0, s1, s2]
    #promedio no es un array de numpy porque se imprime mejor de esta forma
    return promedio


resultados = []

for frase in frases:
    w, s = calcular_vectores(frase, palabras_positivas, palabras_neutrales, palabras_negativas)
    calidad = avg(w)
    sentimiento = producto_escalar(s)
    promedio = promedio_sentimiento(s)
    resultados.append({
        "frase": frase,
        "w": w,
        "s": s,
        "calidad_promedio": calidad,
        "positiva": s[0],
        "neutra": s[1],
        "negativa": s[2],
        "producto_escalar": sentimiento,
        "promedio_sentimiento": promedio
    })

for resultado in resultados:
    print(f"Frase: {resultado['frase']}")
    print(f"w: {resultado['w']}")
    print(f"s: {resultado['s']}")
    print(f"Calidad promedio: {resultado['calidad_promedio']}")
    print(f"Sentimiento positivo: {resultado['positiva']}")
    print(f"Sentimiento neutro: {resultado['neutra']}")
    print(f"Sentimiento negativo: {resultado['negativa']}")
    print(f"Promedio de sentimiento: {resultado['promedio_sentimiento']}")
    print("\n")

frase_mas_positiva = max(resultados, key=lambda x: x['producto_escalar'])
frase_mas_negativa = min(resultados, key=lambda x: x['producto_escalar'])

print(f"La frase más positiva es: '{frase_mas_positiva['frase']}'")
print(f"La frase más negativa es: '{frase_mas_negativa['frase']}'")
