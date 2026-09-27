tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
else:
   consumo = float(input("Digite o consumo mensal de água em m³: "))

#classificação de consumo

   if tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")

   elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

   elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo > 25 :
    
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
   else:
       print("digite algo valido")
