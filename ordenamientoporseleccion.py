#Practica 1.1 Ordenamiento por selección
#Crea ese # de datos de forma aleatoria usando randrange y ordenarlos utilizando la estructura de Ordenamiento por Selección
#EDUARDO MENDOZA GOMEZ
from random import randrange

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('** Tu lista es: ', numeros)
    return numeros

n = int(input('Digita la cantidad de nuemeros que deseas ordenar: ')) #Se pide un numero entero
lista = RandomNumberGenerator(n, 0, 100) #Se genera el array con la input n y los rangos de numeros aleatorios deseados como argumentos del metodo

for i in range(n): #Primer for
    Menor= i
    print('pasada: #', i, lista)
    for j in range(i+1, n): #J necesita iniciar en i+1 para comparar con el siguiente numero
        if lista[j] < lista[Menor]:
            Menor= j #Se actualiza el numero menor si lista[j] es menor que el numero menor que se esta comparando
    save= lista[i] #Variable que guarda el valor menor
    lista[i]= lista[Menor] #Intercambio de posiciones
    lista[Menor]= save

print('** Tu lista ordenada es... ', lista)
# ULTIMA MODIFICACION: Tijuana Baja California, jueves 19 de agosto del 2021
# Modificado por Eduardo Mendoza
