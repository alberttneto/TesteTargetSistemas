fatMensalDist = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'OUTROS': 19849.53}

total = sum(fatMensalDist.values())

for estado, valor in fatMensalDist.items():
    print(estado + ": " + str(round((valor/total)*100, 0)) + '%')