#Meta 1.2 Ordenamiento burbuja
#Imitar la estructura de ordenamiento de burbuja
#EDUARDO MENDOZA GOMEZ
from random import randrange

print('*** I N I C I O    D E L      P R O C E S O ***')

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('Tu lista es: ', numeros)
    return numeros

def OrdenamientoBurbuja(n, numeros): #Metodo que imita la estructura de ordenamiento de burbuja vista en clase
    i = 0
    j = i + 1
    for i in range(n):
        interruptor = False
        if interruptor:
            break
        for j in range(n):
            if numeros[j] > numeros[i]:
                interuptor = True
                numeros[j], numeros[i] = numeros[i], numeros[j]
    return numeros

if __name__ == "__main__":
    n = int(input('Digita la cantidad de nuemeros que deseas ordenar: ')) #Se pide un numero entero
    print('Tu lista ordenada queda de esta forma: ', OrdenamientoBurbuja(n, RandomNumberGenerator(n,0,100))) #Se llaman los dos metodos hechos.

    print('*** F I N    D E L    P R O C E S O ***')

    # ULTIMA MODIFICACION: Tijuana Baja California, martes 17 de agosto del 2021
    # Modificado por Eduardo Mendoza
