"Exercicio Bomba - Contagem regressiva"

from time import sleep
cont: int = int(input("Insira o tempo para Detonação!"))

for cont in range (cont, -1, -1):
    print(cont)
    sleep(1.0)
print('BUM!')