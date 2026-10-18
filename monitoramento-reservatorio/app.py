import colorama

niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]


def definir_cor(nivel):
    if nivel == 1:
        return colorama.Fore.RED
    elif nivel == 2:
        return colorama.Fore.YELLOW
    elif nivel == 3:
        return colorama.Fore.GREEN
    elif nivel == 4:
        return colorama.Fore.CYAN
    elif nivel == 5:
        return colorama.Fore.BLUE


def exibir_nivel(nivel, porcentagem):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]

    print(cor + mensagem + colorama.Style.RESET_ALL)
    print(f"Reservatório: {porcentagem}%")


print("=== MONITORAMENTO DO RESERVATÓRIO ===")

while True:
    porcentagem = int(input("\nDigite a porcentagem de água no reservatório (0 a 100): "))

    if porcentagem < 0 or porcentagem > 100:
        print("Porcentagem inválida!")
        continue

    if porcentagem <= 20:
        nivel = 1
    elif porcentagem <= 40:
        nivel = 2
    elif porcentagem <= 60:
        nivel = 3
    elif porcentagem <= 80:
        nivel = 4
    else:
        nivel = 5

    exibir_nivel(nivel, porcentagem)

    continuar = input("\nDeseja verificar novamente? (s/n): ")

    if continuar.lower() != "s":
        print("Programa encerrado.")
        break