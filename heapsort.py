#Heap sort

from random import randrange

def heapify(lista, i):
    #Si el nodo tiene dos hijos
    if 2 * i + 2 <= len(lista)-1:

        if lista[2 * i + 1] <= lista[2* i +2]:
            min = 2 * i + 1
        else:
            min = 2 * i +2

        if lista[i] > lista[min]:
            lista[i], lista[min] = lista[min], lista[i]

            heapify(lista,min)

    #Si tiene un hijo
    elif 2 * i + 1 <= len(lista)-1:
        if lista[i] > lista[len(lista)-1]:
            if lista[i] > lista[2 * i + 1]:
                lista[i], lista[2 * i + 1] = lista[2 * i + 1], lista[i]

    return lista

def heapSort(lista):
    lista_final = []

    for i in range(len(lista) // 2 - 1, -1, -1):
        lista = heapify(lista, i)

    for i in range(0, len(lista)):
        aux = lista[0]
        lista[0] =lista[len(lista)-1]
        lista[len(lista)-1] = aux

        lista_final.append(aux)

        lista = lista[:len(lista)-1]

        lista = heapify(lista, 0)

    return lista_final

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria #Metodo para generar una lista de numeros aleatorios, dependiendo de los argumentos dados
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('** Tu lista es: ', numeros)
    return numeros

def ask_for_integer(text_to_show): #Metodo para pedir un entero sacado de la clase de Programacion Orientada a Objetos
    while True:
        try:
            num = int(input(text_to_show))
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

    return num

n = ask_for_integer('Digita la dimension del arreglo deseado: ')
lista = RandomNumberGenerator(n, 0, 100)

print(lista)


print(heapSort(lista))