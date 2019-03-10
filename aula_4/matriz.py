

def le_matriz():
	
	M = []
	
	count = 0

	while True:
		linhaStr = input()
		# condicao de parada
		if linhaStr == "":
			break

		linha = linhaStr.split()

		M.append([])

		for item in linha:

			M[count].append(int(item))

		count += 1


	return M

def imprime_matriz(M):
	# imprime matriz
	for linha in M:
		for item in linha:
			print(item, end=' ')
		print("") # para imprimir \n



# chama funcao que le matriz
M = le_matriz()

# chama funcao que imprime matriz
imprime_matriz(M)








