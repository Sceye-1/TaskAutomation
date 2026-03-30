def somar(n1, n2):
    return n1 + n2

def imrpimir(texto):
    print(texto)

def ler():
    return int(input())

def pulaLinha():
    print('\n') 

imrpimir('Digete o numero 1')
n1 = ler()

imrpimir("Digete o numero 2")
n2 = ler ()

resposta = somar(n1, n2)
imrpimir(f'o Resiltado é {resposta}' )