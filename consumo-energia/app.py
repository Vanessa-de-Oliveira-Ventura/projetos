nome = input("Nome do aparelho: ")
potencia = float(input("Potência (W): "))
horas = float(input("Tempo de uso diário (h): "))

custo_kwh = 0.75
consumo_mensal = (potencia * horas * 30) / 1000
custo_estimado = consumo_mensal * custo_kwh

print("\n--- Resultado ---")
print(f"Aparelho: {nome}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")
