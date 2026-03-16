'''
Crie um app que solicite duas notas do usuario, apos calcule a média das nota. Se a media for maior ou igual a 6 
mostre uma mensagem dizendo que o aluno foi aprovado. SE a média for menor que 6, peça para  o aluno digitar a nota do exame final. 
Calcule novamente a média apos o exame final ((média + exame final / 2)). Se a média final for maior que 6 mostre a mensagem aprovado, senão mostre que o aluno foi reprovado.
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Você foi aprovado!")
else:
    exame = float(input("Exame final: "))
    media = (exame + media)/2

    if media > 6:
        print("Arovadinho")
    else:
        print("Reprovado")