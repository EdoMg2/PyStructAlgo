#META 1.3 ordenamiento por inserción
#Objetivo:  Usar el ordenamiento de Inserción directa correctamente creando una lista aleatoria de entre 1 a 50 numeros mostrando en la pantalla cada vez que se cumple un ciclo.
#EDUARDO MENDOZA GOMEZ

from random import randrange

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

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria #Metodo para generar una lista de numeros aleatorios, dependiendo de los argumentos dados
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('** Tu lista es: ', numeros)
    return numeros

n= ask_for_integer('Digita un numero entero entre 1 y 50: ') #Se crea n igualada al valor dado por el usuario

while n>50 or n == 0: #Si el numero no esta dentro del rango pedido, por medio de un while se sigue pidiendo n hasta que cumpla con el rango necesario.
    print('ERROR... Numero mayor a 0 y 50... Intentar de nuevo')
    n = ask_for_integer('Digita un numero entero entre 0 y 50: ')

lista= RandomNumberGenerator(n, 0, 100) #Se crea una lista con la cantidad de numeros dados y que estos esten entre el 0 y el 100

for i in range(1, len(lista)): #Estructura ordenamiento por seleccion

    save = lista[i]
    key = i

    while key > 0 and lista[key- 1] > save:
        lista[key] = lista[key-1]
        key = key-1

    lista[key] = save #Se cambian los valores
    print('Ciclo #',i,': ',lista) #Se imprime cada vez que un ciclo for se cumple

print('Tu lista terminada es:',lista) #Finalmente se imprime la lista ordenada

# ULTIMA MODIFICACION: Tijuana Baja California, martes 24 de agosto del 2021
# Modificado por Eduardo Mendoza
