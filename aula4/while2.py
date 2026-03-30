continuar = True

while continuar:
    print("Digite o nome do aluno: ")
    aluno = input()

    resp = input("Deseja continuar: \nO para Não\n1 para Sim ")
    if resp == "0":
        continuar = False
