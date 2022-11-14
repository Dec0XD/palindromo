frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tdjunto = ''.join(palavras)
inverso = ''
for letra in range(len(tdjunto) - 1, -1, -1):
    inverso += tdjunto[letra]
if inverso == tdjunto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não forma um palindromo!')
