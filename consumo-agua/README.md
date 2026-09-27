# 💧 Consumo de Água
## 🌱 Sobre o projeto
O projeto Consumo de Água foi desenvolvido em Python para classificar o perfil de consumo de imóveis e apresentar mensagens educativas aos moradores.
O sistema considera três tipos de imóveis:
- 🏢 Comercial
- 🏠 Casa
- 🏢 Apartamento
A classificação é feita de acordo com o tipo de imóvel e o consumo mensal de água em metros cúbicos (m³).
## 🎯 Objetivo
O objetivo é utilizar a programação para identificar diferentes situações de consumo de água e apresentar orientações de conscientização ambiental.
## 🐍 Tecnologias utilizadas
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)
## ▶️ Como executar
1. Tenha o Python instalado no computador.
2. Baixe ou clone este repositório.
3. Abra a pasta `consumo-agua`.
4. Execute o arquivo `app.py`.
5. Informe o tipo de imóvel e o consumo mensal de água.
## 📋 Regras de classificação
### 🏢 Imóvel comercial
Exibe:
> Tarifa comercial aplicada – consulte o plano corporativo.
### 🏠 Apartamento com consumo menor que 10 m³
Exibe:
> Consumo econômico – excelente controle de água!
### 🏠 Apartamento ou casa com consumo de até 25 m³
Exibe:
> Consumo moderado – dentro do padrão residencial.
### ⚠️ Acima do limite residencial
Exibe:
> Consumo excessivo – adote medidas de economia e verifique vazamentos.
## 📁 Estrutura do projeto
```text
consumo-agua/
├── app.py
└── README.md


# Sistema de classificação do consumo de água

# Entrada de dados
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classificação do consumo
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
