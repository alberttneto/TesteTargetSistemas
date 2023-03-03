import json


with open('dados.json', 'r') as f:
    data = json.load(f)

ValorFatMes = [x['valor'] for x in data]
ValorFatMesDiasUteis = [x for x in ValorFatMes if x != 0]
mediaMensal = sum(ValorFatMesDiasUteis)/ len(ValorFatMesDiasUteis)

menorValorFatMes =  min(ValorFatMes)
menorValorFatDiasUteis = min(ValorFatMesDiasUteis)
maiorValorFatMes = max(ValorFatMes)
diasFatSup = sum([1 for x in ValorFatMesDiasUteis if x > mediaMensal])


print("O menor valor de faturamento ocorrido em um dia do mês: ", menorValorFatMes)
print("O menor valor de faturamento ocorrido em um dia util do mês: ", menorValorFatDiasUteis)
print("O maior valor de faturamento ocorrido em um dia do mês: ", maiorValorFatMes)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", diasFatSup)
