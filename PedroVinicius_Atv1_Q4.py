def forca(x=0):
    if x == 0:
        print("------------")
        print("|          |")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")
    elif x == 1:
        print("------------")
        print("|          |")
        print("|          0")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")
    elif x == 2:
        print("------------")
        print("|          |")
        print("|          0")
        print("|          |")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")
    elif x == 3:
        print("------------")
        print("|          |")
        print("|          0")
        print("|         -|")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")
    elif x == 4:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|")
    elif x == 5:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|         /      ")
        print("|               ")
        print("|               ")
        print("|")
    elif x == 6:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|         / \\    ")
        print("|               ")
        print("|    Lamento, Você foi Enforcado! ")
        print("|")


erros = 0

word = input('Informe a palavra: ')
temp = []
i = 0
for letra in word:
    temp.append('_')


while True:
    print('\n' * 20)
    forca(erros)
    print('\n\nAdivinhe: ', end='')
    for let in temp:
        print(let, end=' ')
    print('\n' * 2)

    if erros == 6:
        break
    ganhouJogo = True
    for let in temp:
        if let == '_':
            ganhouJogo = False
    if ganhouJogo:
        print('\nPARABÉNS VOCÊ VENCEU!!!')
        break
    valid = False
    c =[]
    while (valid == False):
        valid = True
        t = len(temp)
        chut = input("Informe uma letra: ")
        if(not t == 0):     
            for i in range(t):
                if (chut == temp[i]):
                    print('Letra já Informada Anteriormente')
                    valid = False
                    break
            else:
                    if (i == t-1):
                        c.append(chut)
        else:
            c.append(chut)

    errouLetra = True
    for i, let in enumerate(word):
        if word[i] == chut:
            temp[i] = word[i]
            errouLetra = False
    if errouLetra:
        erros = erros + 1
