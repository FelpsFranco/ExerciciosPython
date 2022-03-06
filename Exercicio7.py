#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

def soma(lista_soma):
    i = 0
    for recebe in range(5):
        i = i + 1
        number = int(input('Digite o {}° valor -> '.format(i)))
        lista_soma.append(number)
    print('A sua lista é: ', lista_soma)
    print('A soma dos valores é: ', sum(lista))

def multi(lista_mult):
    multi = 1
    for numero in lista_mult:
        multi *= numero
    print('A multiplicação dos valores é: ', multi)


lista = []
soma(lista)
multi(lista)






