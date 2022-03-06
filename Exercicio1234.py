def insere(j, vetors):
    while(j < 6):
        j = j + 1
        number = int(input('Digite um valor para ser inserido: '))
        vetors.append(number)
    return vetors

def reverso(vetor_reverso):
    vetor_reverso.reverse()
    return vetor_reverso

def soma(vetor_soma):
    print('A soma é: ',sum(vetor_soma))

def media(vetor_media):
    media = sum(vetor_media)/5
    print('A média é: {}'.format(media))

def vetor_letras(letras):
    i = 0
    while i < 11:
        i = i + 1
        letra = str(input('Digite uma Letra: '))
        letras.append(letra)
    return letras

def verifica_vogal(lista_vogal):
    new_lista = ['a', 'e', 'i', 'o', 'u']
    verifica = [letra for letra in lista_vogal]
    for a in new_lista:
        if a in lista_vogal:
            verifica.remove(a)
    print('Lista de Vogais: ', verifica)


def verifica_conso(lista_conso):
    new_lists = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    res = [letra for letra in lista_conso]
    for a in new_lists:
        if a in lista_conso:
            res.remove(a)
    print('Lista sem Consoantes',res)


vetor = []
i = 1
lista_letras = []
print('Vetor')

insere(i, vetor)
print(vetor)

reverso(vetor)
print(vetor)

soma(vetor)
media(vetor)

vetor_letras(lista_letras)
print('Lista Criada',lista_letras)

verifica_conso(lista_letras)
verifica_vogal(lista_letras)
