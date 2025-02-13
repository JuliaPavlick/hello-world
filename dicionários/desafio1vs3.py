
texto = "programacao"
contagem = Counter(texto)

for letra, quantidade in contagem.items():
    print(letra, quantidade, sep='')
