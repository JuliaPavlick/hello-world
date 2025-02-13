from collections import Counter

def contar_letra(s):
    contagem = Counter(s)
    for letra, quantidade in contagem.items():
        print(f"Letra '{letra}': {quantidade} vezes")

texto = "programacao"
contar_letra(texto)
