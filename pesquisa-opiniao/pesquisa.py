# Pesquisa de Opinião - TudoWeb

excelente = 0
bom = 0
ruim = 0

# Pesquisa com 50 entrevistados
for i in range(50):
    print("\n--- Entrevistado", i + 1, "---")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção: "))

    # Verificação da opinião
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom+=1
    elif opiniao == 3:
        ruim += 1
    else:
        print("opção invalida")
# Exibição do resultado
print("\n--- Resultado da Pesquisa ---")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas BOM:", bom)
print("Quantidade de respostas RUIM:", ruim)