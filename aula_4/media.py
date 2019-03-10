def calcula_media(items):
	soma = 0.0
	numItems = len(items)

	for item in items:
		soma += float(item)

	media = soma/numItems
	
	return media


def procura_elementos(items, media):
	print("items maiores que a média:")
	for item in items:
		if float(item) > media:
			print(item)

# le entrada
entradaStr = input()

if entradaStr == "":
	print("Entrada Vazia")
else:

	items = entradaStr.split()
	#chama funcao que calcula media
	media = calcula_media(items)

	print("Media: %.2f " % media)
	
	procura_elementos(items, media)
