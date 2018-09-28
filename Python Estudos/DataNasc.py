Meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
DataN = input("Digite seu nascimento no formato DD-MM-AAAA: ")
MesN = int(DataN[3:5:1])
print("Voce nasceu no mes de "+ Meses[(MesN - 1)])
idm = int(input("Id do mes: "))
mesid = input("Nome do mes: ")
mesrem = Meses.pop(idm - 1)
mesint = Meses.insert((idm -1), mesid)
print(Meses)