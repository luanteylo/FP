menorPreco = None

while True:  
  entrada = input()
  
  if entrada == "":
    break
  
  quantidade = float(entrada.split()[0])
  preco = float(entrada.split()[1])
  
  if preco > maiorPreco:
    maiorPreco = preco    

print("O item de menor preço: ", menorPreco)
