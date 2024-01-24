#Practica #1.2 Ordenamieento por Mezcla
#Objetivo:  Aplicar correctameente el ordenamiento por mezcla y mostrar el numero de veces que se modifico la lista
#EDUARDO MENDOZA GOMEZ

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

def mergeSort(A, l, r, contador): #contador es necesario para la impresion del numero de modificaciones
    if l < r:
        m = l + (r - l) // 2

        mergeSort(A, l, m,contador)
        mergeSort(A, m + 1, r, contador)
        merge(A, l, m, r,contador)
        contador= contador + merge(A, l, m, r,contador)

        #Contador es usado de esta forma para que no tenga un reinicio cada vez que se vuelve a llamar al metodo
        return contador #contador es devuelto como dato para que sea impreso

def merge(A,l,m,r,cont): #cont cumple con el papel de contador
    #Numeros auxiliares
    t1 = m - l + 1
    t2 = r - m
    #Se crean arreglos temporales
    B = [0] * (t1)
    C = [0] * (t2)

    # Se copian los datos para los anteriores arreglos B Y C
    for i in range(0, t1):
        B[i] = A[l + i]

    for j in range(0, t2):
        C[j] = A[m + 1 + j]
    #Indices para los arrays creados
    i = 0  #B
    j = 0  #C
    k = l  #Indice para el array mezclado

    while i < t1 and j < t2:
        if B[i] <= C[j]:
            A[k] = B[i]
            cont +=1
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    # Se copian los elementos restantes de B siempre si queda uno
    while i < t1:
        A[k] = B[i]
        cont += 1

        i += 1
        k += 1

    # Se copain los elemntos restantes de C siempre si queda uno
    while j < t2:
        A[k] = C[j]
        cont +=1

        j += 1
        k += 1
        return cont
        #Cont es devolvido a mergeSort


n = ask_for_integer('Digita la cantidad de numeros que quieres en tu array: ') #Se pide la cantidad de numeros deseados dentro del array

while n > 20: #While para que el numero pedido no sea mayor a 20
    n = ask_for_integer('ERROR... Digita la cantidad de numeros que quieres en tu array, no debe de ser mayor a 20: ')

arr = []
# Recolecta los datos para formar el array
for i in range(0, n):
    ele = int(input())

    arr.append(ele)

print("Array dado es:",arr)


mergeSort(arr, 0, n - 1, 0)
print("\nArray ordenado es:",arr)#Se imprime el arreglo ordenado
print('el numero de veces que se modifico es:', mergeSort(arr, 0, n - 1, 0)) #Se imprime el numero de repeticiones

# ULTIMA MODIFICACION: Tijuana Baja California, jueves 26 de agosto del 2021
# Modificado por Eduardo Mendoza