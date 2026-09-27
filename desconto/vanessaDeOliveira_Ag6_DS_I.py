# Entrada de dados
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verificação da faixa de desconto
if valor_compra < 200:
    desconto = 0.05
elif valor_compra < 300:
    desconto = 0.10
else:
    desconto = 0.15

# Cálculo do desconto e do valor final
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

# Exibição dos resultados
print("\n--- Resumo da compra ---")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")

# Mensagem de agradecimento
print("\nObrigada por comprar na VGL, volte sempre!")
