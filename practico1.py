import numpy as np

with open('frases.txt', 'r', encoding='utf-8') as f:
    frases = f.readlines()

frases = [frase.strip() for frase in frases]

palabras_positivas = {
    "excelente", "gran", "positivo", "maravilloso", "increíble", 
    "feliz", "fantástico", "espléndido", "optimista", "alegría", 
    "éxito", "genial", "felicidad", "beneficio", "logro"
}

palabras_neutrales = {
    "pérdida", "cambio", "necesidad", "circunstancia", "situación",
    "espera", "moderado", "simple", "promedio", "condición", 
    "rutina", "transición", "detalles", "acción", "procedimiento"
}

palabras_negativas = {
    "muerte", "luto", "fracaso", "depresión", "problema", 
    "triste", "negativo", "dolor", "sufrimiento", "miedo", 
    "pérdida", "caída", "daño", "error", "derrota"
}

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

def promedio_sentimiento(s):
    sentimiento_base = np.array([1, 0, -1])
    return np.dot(sentimiento_base, s)

resultados = []

for frase in frases:
    w, s = calcular_vectores(frase, palabras_positivas, palabras_neutrales, palabras_negativas)
    calidad = avg(w)
    sentimiento = promedio_sentimiento(s)

    resultados.append({
        "frase": frase,
        "w": w,
        "s": s,
        "calidad_promedio": calidad,
        "positiva": s[0],
        "neutra": s[1],
        "negativa": s[2],
        "promedio_sentimiento": sentimiento
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

frase_mas_positiva = max(resultados, key=lambda x: x['promedio_sentimiento'])
frase_mas_negativa = min(resultados, key=lambda x: x['promedio_sentimiento'])

print(f"La frase más positiva es: '{frase_mas_positiva['frase']}'")
print(f"La frase más negativa es: '{frase_mas_negativa['frase']}'")
