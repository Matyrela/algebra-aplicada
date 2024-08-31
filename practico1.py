import numpy as np

frases = [
    "Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional",
    "Fue un día maravilloso lleno de éxito y alegría.",
    "El proyecto fue genial y el resultado fue increíble.",
    "Estoy feliz por el logro y el beneficio obtenido en el trabajo.",
    "El ambiente fue fantástico y optimista durante toda la reunión.",
    "Tener una actitud fantástica puede llevarte al éxito y a la felicidad.",
    "La empresa está en una fase de transición y cambio debido a las circunstancias.",
    "Es importante analizar cada situación y necesidad de manera moderada.",
    "El procedimiento fue un simple trámite, sin demasiados detalles.",
    "Estamos evaluando los detalles y condiciones actuales para tomar decisiones.",
    "La necesidad de un cambio fue evidente en las circunstancias actuales.",
    "La noticia de la muerte lo dejó en luto y lleno de sufrimiento.",
    "Fue un día lleno de sufrimiento, dolor y tristeza.",
    "El proyecto terminó en un fracaso debido a un error y causó mucho dolor.",
    "Sentí un profundo miedo por la posible caída y el fracaso del proyecto."
]


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
    w = np.array([1 if palabra in palabras else 0 for palabra in todas_palabras])

    s = np.array([
        np.sum([palabra in palabras for palabra in positivas]),  # Positivas
        np.sum([palabra in palabras for palabra in neutrales]),  # Neutrales
        np.sum([palabra in palabras for palabra in negativas])  # Negativas
    ])

    return w, s

def avg(w):
    x = 0
    for num in w:
        x += num

    return x / len(w)

    # return np.mean(w)

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
        "promedio_sentimiento": sentimiento
    })

for resultado in resultados:
    print(f"Frase: {resultado['frase']}")
    print(f"w: {resultado['w']}")
    print(f"s: {resultado['s']}")
    print(f"Calidad promedio: {resultado['calidad_promedio']}")
    print(f"Promedio de sentimiento: {resultado['promedio_sentimiento']}")
    print("\n")

frase_mas_positiva = max(resultados, key=lambda x: x['promedio_sentimiento'])
frase_mas_negativa = min(resultados, key=lambda x: x['promedio_sentimiento'])

print(f"La frase más positiva es: '{frase_mas_positiva['frase']}'")
print(f"La frase más negativa es: '{frase_mas_negativa['frase']}'")