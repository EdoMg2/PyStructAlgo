#Practica #1.2 Shell sort
"""
    Objetivos:

1.- Solicita al usuario el # de elementos del arreglo

2.- Captura en una línea separada por espacios los elementos correspondientes al arreglo [Valida que sean los que pidio el usuario].

3.- implementa el ordenamiento Shell

4.- Solicita al usuario un valor númerico el cual buscaras en la lista.

5.- Implementa la busqueda binaria, y si el elemento se encuentra en la lista, menciona cuantos elementos existen en la lista antes que él, si no existe, muestra el mensaje "Valor no encontrado".

"""
#EDUARDO MENDOZA GOMEZ 33069


def busqueda_binaria(lista, numero):
    #inicio y final funcionan como variables para delimitar el arreglo
    inicio = 0
    final = len(lista) - 1
    #Comprobacion es usado cuando el numero que se quiere buscar no se encuentra en el arreglo
    Comprobacion = False
    #j funciona como contador del numero de veces que se dividio el arreglo para encontrar el numero e inicia en uno porque siempre hara una particion
    j = 1
    #Ciclo while para que se repitira hasta que se encuentre el numero o se exploren todos
    while inicio <= final:
        #medio funciona como la mitad del arreglo delimitado por inicio y final
        medio = (inicio+final) // 2
        if numero == lista[medio]:
            #Si se encuentra el numero se acaba el ciclo, se imprime donde se encontro, la cantidad de numeros detras de el y el numero de veces que se repitio el ciclo para encontrarlo
            print(f'Se encontro {numero} en la posicion [del arreglo]: {medio}, por lo que hay {medio} numeros detras de el')
            print('**EL NUMERO DE PARTICIONES FUE DE:', j)
            return medio
            Comprobacion = True

        elif numero > lista[medio]:
            #Si el numero es mayor a la mitad, se descarta la mitad inferior al numero para solamente buscar en la parte que es superior al numero
            inicio = medio + 1
        else:
            #Si el numero es menor a la mitad, se descarta la mitad superior al numero para solamente buscar en la parte que es inferior al numero
            final = medio - 1
        #j aumenta en uno cada vez que hay una particion o cambio de inicio o final
        j= j+1
    #Si no se encontro el numero Comprobacion no cambiara a True por lo que se imprimira que el numero no se encuentra en la lista.
    if Comprobacion == False:
        print('WOOPS!...Parece que el valor no se encuentra dentro del arreglo..intente de nuevo......')

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

def shellSort(lista):
    #Se imprime la lista que se da como parametro
    print('\n**Tu lista ordenada es:', lista)
    #size es la ultima posicion de la lista
    size = len(lista)-1
    #inte es la cantidad de numeros en la lista
    inte = size+1
    #contador para cada vez que hay un cambio en la lista
    j=1
    #Ciclo while hasta que inte llegue a 1
    while inte > 1:
        #Cada vez que se repite el ciclo, inte se divide a la mitad para funcionar como la distancia del salto
        inte = (inte//2)
        #Se establece band como verdadero
        flag = True
        #Se crea el segundo ciclo
        while flag == True:
            flag = False
            #i funciona como el numero de la posicion que se ira comparando
            i= 0
            #Se crea el tercer ciclo que se cumplira mientras la posicion que se comparara con i llegue hasta el final del arreglo
            while i+inte <= size:
                #Se compara la posicion i con la distancia del salto + i
                if lista[i]> lista[i+inte]:
                    #si la posicion de la izquierda es inferior a la de la derecha cambiaran de posicion
                    lista [i], lista[i+inte] = lista[i+inte], lista[i]
                    #Se imprime el numero de corrida con cambio y la lista
                    print(f'#{j}: {lista}')
                    #j avanza en 1 y band vuelve a True si se cumple la condicion para que se repita el ciclo
                    j= j+1
                    flag = True
                #i avanza una posicion
                i = i+1
                #la posicion ira avanzando de 1 en 1

    #Se imprime la lista ordenada
    print('\n**Tu lista ordenada es:', lista)
    #Se pide el numero que se desea buscar con la busqueda binaria
    numero = ask_for_integer('\nDigita el numero que deseas buscar: ')
    #Se llama la funcion busqueda_binaria con la lista ordenada y el numero pedido como parametros
    busqueda_binaria(lista, numero)

#Se inicia un Try para perdir la lista que se desea introducr
try :
    n= ask_for_integer('\nDigita la cantidad de numeros que deseas: ') #Se llama la funcion para tener el arreglo de numeros deseados
    lista_0 = input('Digita los numeros que vas a utilizar (Separados por un espacio): ') #Se recolectan los datos
    #cada numero se separara por el espacio entre ellos y se crea el arreglo
    lista= [int(n) for n in lista_0.split(' ')]
    #lista sera el nombre del arreglo utilizado
    #Se comprueba que la cantidad de datos ingresados sea el mismo que la cantidad introducida al principio
    n2= len(lista)

    #Si no coinciden el programa se acabara
    if n2 != n:
        print('ERROR!.... Los numeros introducidos no coincide con la cantidad deseada')
        exit(1)
#evita que se ingresen datos que no sean enteros
except ValueError:
    print('Solo se permiten numeros...')
    exit(1)

#Se llama la funcion shellSort
shellSort(lista)

# ULTIMA MODIFICACION: Tijuana Baja California, martes 31 de agosto del 2021
# Modificado por Eduardo Mendoza 33069