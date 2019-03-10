"""
O programa calcula o abono salarial
que uma empresa concederá aos seus
funcionários com mais de um ano de 
tempo de serviço.

Os que tem menos de dez anos ganharão
abono de 10%. Os demais ganharão 25%.
"""

salario = float(input("Digite o salario: "))
tempo = int(input("Digite o tempo de serviço (em anos): "))

if tempo <= 1:
	print("Não tem abono =/")
else:
	if tempo < 10:
		abono = salario * 0.10
	else:
		abono = salario * 0.25

	print ("Abono: ", abono)
	print("Novo salario: ", salario + abono)









