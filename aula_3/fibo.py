def fib_rec(n):
	if n == 0:
		return 0
	if n == 1:
		return 1

	return fib_rec(n -1) + fib_rec(n -2)

def fib_interativo(n):
	vet = [0, 1]

	for i in range(2, n+1):
		vet.append(vet[i-1] + vet[i-2])

	return vet[n]

n = int(input("digite o valor: "))

op = int(input("digite a opção:\n1 - fibonacci recursivo\n2 - fibonnaci iterativo\n"))

if op == 1:
	print("Fib: ", fib_rec(n))
elif op == 2:
	print("Fib: ", fib_interativo(n))
else:
	print("Opcao invalida!")
	