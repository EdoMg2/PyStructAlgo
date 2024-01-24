# TAREA 1.5 ESTRUCTURA DE DATOS - MERGE SORT
# POR SEBASTIAN ROSALES MARTINEZ 284063 ICE

def mergeSort(arr):
    if len(arr) > 1:

        # Diviendo el array por la mitad
        mid = len(arr) // 2

        # Dividimos los elementos dentro del array, estos son los elementos de la izquiersa
        L = arr[:mid]

        # se dividen unicamente entre 2 para formar pares en su mayoria
        R = arr[mid:]

        # En este se ordena la primera mitad, la mitad de la izquierda
        mergeSort(L)

        # Ordenamos la mitad de la derecha.
        mergeSort(R)

        i = j = k = 0

            # SOMETEMOS A EVALUACION AMBOS EXTREMOS
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Este while será encargado de revisar que los elementos se encuentren en orden y checar que no hayan
        # cabos sueltos
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(arr,"N de movimientos: ", i)

# El siguiente for se encargará de imprimir las listas


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()



if __name__ == '__main__':
    # Creamos una lista vacia para llenarla, este es el primer paso de todos, es importante
    # crear un for para repetir la entrada de los datos
    arr = []

    # En esta instancia utilizamos una variable n para definir la cantidad de elementos
    # que conformaran la lista, esta variable sera añadida a nuestro for.
    n = int(input("Introduce el numero de elementos de la lista : "))

    # El for creará una interación desde 0 hasta el valor introducido en la variable n.
    for i in range(0, n):
        ele = int(input())

        arr.append(ele)  # añadimos el elemento por medio del appendice

    print('Los valores introducen crean la siguiente lista:\n',arr)

    print("La lista inicial es: ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("La lista organizada es: ", end="\n")
    printList(arr)

#ULTIMA MODIFICACION 26 DE AGOSTO DEL 2020 A LAS 11:41 AM, TIJUANA BAJA CALIFORNIA