print('    ')
valor = int(input('insira Valor: '))
taxa = int(input('insira Taxa: '))
tempo = int(input('insira Tempo: '))
print('    ')
prestação = valor+(valor*taxa/100)*tempo

print('O Valor da Prestação em Atraso é: ', prestação)
print('    ')