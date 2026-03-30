'''
Crie um script que solicita que o usario digite dois numero, apos mostre o resultado da visão do primeiro pelo segundo numero.
'''
try:
    num1 = int(input("! "))
    num2 = int(input("! "))
    resultado = num1 / num2
    print("Resultado: ", resultado)
except ValueError:
    print("deu erro pai")
except ZeroDivisionError:
    print("Você não pode dividir por 0")
except Exception as e:
    print("Ocorreu um erro ai", e)
