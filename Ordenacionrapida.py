#META Ordenación rapida
#EDUARDO MENDOZA
#Instrucciones:
"""
a) Captura un # entero n, donde 1<= n <= 50

b) Genera de forma aleatoria los “n” elementos de la lista (del 1 al 100)

c) Usar el ordenamiento de QUICK SORT

d) Salida, muestra en pantalla todas las corridas necesarias hasta llegar a la lista ordenada. No olvides mostrar los datos de inicio.
def quickSort(lista, inicio, final):

"""

from random import randrange

def ask_for_integer(text_to_show): #Metodo para pedir un entero sacado de la clase de Programacion Orientada a Objetos
    while True:
        try:
            n = int(input(text_to_show))
            break
        except ValueError:
            print('INVALID: Please input integer only. . .')
            continue
        except SyntaxError:
            print('INVALID: Please input integer only. . .')
            continue
        except NameError:
            print('INVALID: Please input integer only. . .')
            continue

    return n

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria #Metodo para generar una lista de numeros aleatorios, dependiendo de los argumentos dados
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('** Tu lista es: ', numeros)
    return numeros

def QuickSort(A, l, r):
    if l>r:
        return A
    m = Partition(A,l,r) #Se ejecuta el metodo de particion para encontrar la posicion del pivote
    #print('menor al pivote m (%i) son:'%A[m], A[l:m-1]) #Formas alternativas de mostrar las corridas necesarias
    #print('mayor al pivote m (%i) son:'%A[m], A[m+1:r])
    QuickSort(A,l,m-1) #Se llama la particion para los numeros detras del pivote
    QuickSort(A,m+1,r) #Se llama la particion para los numeros despues del pivote

    return A

def Partition(A,l,r): #Metodo para la particion
    pivot = A[r] #En este programa el pivote empieza en el ultimo espacio del arreglo
    j = l #Se Crea j para que sirva como contador auxiliar
    for i in range(l,r):
        if A[i] < pivot: #Cada vez que el pivote sea mas grande que el numero que el numero del arreglo que esta comparando se cambiaran de posicion el espacio j con el i
            print('El numero %i cambiara posicion con:'%A[i],A[j],', Y la lista esta se encuentra el siguiente estado: ', A) #Forma elegida para mostrar las corridas necesarias
            A[j], A[i] = A[i], A[j]
            j = j+1 #j avanzara una posicion

    print('El pivote %i cambiara posicion con:' % A[r], A[j], ', Y la lista se encuentra en el siguiente estado: ', A) #Forma elegida para mostrar cada vez que hay un cambio de pivote
    A[j], A[r] = A[r], A[j] #El pivote cambiara posicion con la ultima posicion de j.

    return j #Se regresa j como dato para el metodo QuickSort

n= ask_for_integer('Digita un numero entero entre 1 y 50: ') #Se crea n igualada al valor dado por el usuario

while n>50 or n == 0: #Si el numero no esta dentro del rango pedido, por medio de un while se sigue pidiendo n hasta que cumpla con el rango necesario.
    print('ERROR... Numero mayor a 0 y 50... Intentar de nuevo')
    n = ask_for_integer('Digita un numero entero entre 0 y 50: ')

lista= RandomNumberGenerator(n, 0, 100) #Se crea una lista con la cantidad de numeros dados y que estos esten entre el 0 y el 100

n = len(lista)
QuickSort(lista, 0, n-1)
print("** Tu lista ordenada es: ", lista)

# ULTIMA MODIFICACION: Tijuana Baja California, martes 24 de agosto del 2021
# Modificado por Eduardo Mendoza