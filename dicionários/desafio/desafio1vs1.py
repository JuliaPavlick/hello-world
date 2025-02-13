
from collections import Counter

def letra_mais_comum(s):
   
    contagem = Counter(s)
   
    letra_mais_frequente = max(contagem, key=contagem.get)
    return letra_mais_frequente

texto = "programacao"
print(letra_mais_comum(texto))  