valores = []

n = 5

for i in range(n):
	v = float(input("digite o valor: "))
	valores.append(v)

soma = 0.0
for i in range(n):
	soma = valores[i] + soma

print("Media: ", soma/n)