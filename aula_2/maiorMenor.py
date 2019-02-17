# Dado uma entrada contendo 5 valores
# Imprima o maior numero.

maior = None
menor = None

for i in range(5):
  x = int(input())
  if maior is None or x > maior:
    maior = x
   
  if menor is None or x < menor:
    menor = x

print("o maior numero foi: ", maior)
print("O menor numero foi: ", menor)

