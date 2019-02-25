 
n = int(input("digite a quantidade de valores: "))

soma = 0.0

for i in range(n):
	x = int(input("digite o valor: "))
	soma = soma + x

print("A media eh: ", soma/n)