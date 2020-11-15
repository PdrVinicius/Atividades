print(' ')
p1 = float(input('Insira Nota da Primeira Prova: '))
p2 = float(input('Insira Nota da Segunda Prova: '))
p3 = float(input('Insira Nota da Terceira Prova: '))
freq = int(input('Insira a Porcetagem da Frequencia: '))

mf = (p1+p2+p3)/3

print(' ')

if (freq<75) or (mf<7):
    print('O Aluno está Reprovado devido a sua Frequencia ou Média Final que São: ', freq, ', ', mf)
else:
    print('O Aluno está Aprovado, Sua Frequencia e Média Final São: ', freq, ', ', mf)
print(' ')