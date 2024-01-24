#META 1.5 HeapSort
"""
Utiliza el programa en Python proporcionado por tu docente, y Documenta de manera explicita y clara, que es lo que hace este programa.

"""
#EDUARDO MENDOZA GOMEZ

# Funcion heapsort que funciona al enviar un arreglo como parametro
def heapsort(a):
    #Se llama la funcion heapify con el arreglo a y la cantidad de elementos en el arreglo como parametros
    heapify(a, len(a))
    #Se establece end como la posicion final del arreglo a
    end = len(a)-1

    #Ciclo while que acabara hasta que end llegue a 0
    while end > 0:
        #Se intercambian las posiciones del primer y ultimo numero del arreglo a
        a[end], a[0] = a[0], a[end]
        #end disminuye en 1 cada vez que se cumple un ciclo
        end -= 1
        #Se llama la funcion sift_down con la lista modificada, 0, y la variable end como parametros
        sift_down(a, 0, end)

     #Por ultimo el metodo ordenara la lista

#Funcion heapify que empieza a trabajar cuando recibe una lista y la extencion de esta
def heapify(a,count):
    #Se crea la variable start que sera igual al redondeo de la posicion final menos 1 y dividido entre 2
    start = int((count-2)/2)
    #Se imprime el valor de start para indicar cual fue la posicion inicial que se tomo
    print('posicion inicial',start)
    #Ciclo while que acabara hasta que start llegue a 0
    while start >= 0:
        #Se llama la funcion sift_down con la lista, la variable start y la ultima posicion del arreglo como parametros
        sift_down(a,start, count-1)
        #Start disminuira en 1 cada vez que se cumple un ciclo
        start -= 1

#Funcion heapify que empieza a trabajar cuando recibe una lista, un inicio y un final
def sift_down(a,start,end):
    #Root funciona como la raiz de nuestro arbol y es igualada con la posicion inicial
    root = start
    #Mientras la posicion del hijo sea menor o igual que la ultima posicion de la lista final
    while (root*2+1) <= end:
        #La variable child funciona como las posicion hijo de la raiz y esta es la posicion de la raiz + 1 debido a que en python se inicia con la posicion 0 se ocupa el +1
        child = root * 2 +1
        #Se declara la posicion swap que funcionara como un auxiluar y esetara igualada a la posicion raiz
        swap = root
        # Si el valor de a en la posicion swap (que puede ser child, child +1 o root) es menor al valor de a en la posicion child swap cambia su valor al de child
        if a[swap] < a[child]:
            swap = child
        # Si child + 1 (hijo 2) es menor a la ultima posicion del arreglo y el valor de del arreglo a en swap es menor al valor de a en el hijo 2  swap adaptara el valor del hijo 2
        if (child+1) <= end and a[swap] < a[child+1]:
            swap = child+1
        #Si swap es distinto al valor de root (si se cumplio alguna de las otras 2 condiciones) se intercambian los valores en la posicion root con el de la posicion swap
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            #la nueva raiz sera el valor que swap adopto
            root = swap
        #En caso de no cumplirse ningun if anterior, el ciclo continuara
        else:
            return
        #Se imprime como queda la lista despues de cada corrida de esta funcion cuando es llamada por el while de la funcion heapify
        print(a)

#Se crea una lista de prueba
a= [13, 0, 45, 10, 3, 22, 7]
#Se imprime la lista al inicio
print(f'La lista es: {a}')
#Se llama el metodo heapsort que ordenara la lista
heapsort(a)
#Finalmente se imprime la lista ordenada
print (f'Tu lista ordenada es: {a}')

# ULTIMA MODIFICACION: Tijuana Baja California, jueves 24 de agosto del 2021
# Modificado por Eduardo Mendoza
