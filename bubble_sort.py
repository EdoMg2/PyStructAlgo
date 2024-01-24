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

def validar_int (numero,text): #Funcion para validar que lo que se teclea sea un numero

    while True:
        try:
            #En caso de lo que se mande sea un 0 se regresara un 0, esto se hizo denbido a que int('0') no era detectado
            if numero == ' 0':
                break
                return 0
            #num sera la cadena que se mande convertida a entero
            num = int(numero)
            #Se regresa el numero y se acaba la funcion
            return num
            break
        #Excepts para errores comunes que pasan si la cadena que se envia no es verdadero
        except ValueError:
            #Se imprime el mismo mensaje que en los otros errores
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')
            # En todos los errores se regresa un False y se acaba la funcion
            return False
            break
        except SyntaxError:
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')

            return False
            break
        except NameError:
            print(f'INVALIDO: Solo digite enteros despues de "{text}". . .')

            return False
            break

def RandomNumberGenerator(n, Inicio, Final):  #Metodo para genera una lista de numeros aleatoria #Metodo para generar una lista de numeros aleatorios, dependiendo de los argumentos dados
    print('Se esta generando tu lista...')
    numeros= [randrange(Inicio, Final) for i in range(n)]
    print('** Tu lista es: ', numeros)
    return numeros

def lista_por_enters():
    arr = []
    # En esta instancia utilizamos una variable n para definir la cantidad de elementos
    # que conformaran la lista, esta variable sera añadida a nuestro for.
    n = ask_for_integer("Introduce el numero de elementos de la lista : ")

    # El for creará una interación desde 0 hasta el valor introducido en la variable n.
    for i in range(n):
        ele = ask_for_integer('')

        arr.append(ele)  # añadimos el elemento por medio del appendice

    print('Los valores introducen crean la siguiente lista:', arr)

    return arr

def lista_separada(separacion): #funcion para crear una lista a partir de un solo input
    # Se inicia un Try para perdir la lista que se desea introducr
    try:
        n = ask_for_integer('\nDigita la cantidad de numeros que deseas: ')  # Se llama la funcion para tener el arreglo de numeros deseados
        lista_0 = input('Digita los numeros que vas a utilizar (Separados por un espacio): ')  # Se recolectan los datos
        # cada numero se separara por el espacio entre ellos y se crea el arreglo
        lista = [int(n) for n in lista_0.split(separacion)]
        # lista sera el nombre del arreglo utilizado
        # Se comprueba que la cantidad de datos ingresados sea el mismo que la cantidad introducida al principio
        n2 = len(lista)

        # Si no coinciden el programa se acabara
        if n2 != n:
            print('ERROR!.... Los numeros introducidos no coincide con la cantidad deseada')
            exit(1)
    # evita que se ingresen datos que no sean enteros
    except ValueError:
        print('Solo se permiten numeros...')
        exit(1)

    return lista

def bubble_sort(lista): #Funcion para ordenar una lista utilizando la estructura bubble sort
    flag = False #Se crea variable bandera de la que dependera el ciclo while
    j = 1 #Contador para mostrar el numero de cambios que han habido
    while flag == False:
        #cada vez que se inicia el ciclo la bandera sera True para cuando no haya ningun cambio se acabe el while
        flag = True
        #For que ira comparando cada numero de la lista con el siguiente hasta el ultimo
        for i in range(len(lista)-1):
            #Si el numero que se compara es mayor al siguiente de la lista se intercambiaran de posiciones
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                #Se imprime el numero de ciclo que va del while y for
                #Si hubo un cambio la bandera cambiara a False y continuara el bucle while
                flag = False
            print(f'#{i}:', lista)

        #El contador aumenta en uno
        j += 1

def selection_sort(lista): #Funcion para ordenar una lista utilizando la estructura de ordenamiento por insercion
    for i in range(len(lista)): #Primer ciclo for que iniciara con la posicion 0
        #Se crea la variable menor con el valor de el numero de ciclos cumplidos del primer for
        menor = i
        #Segundo for usando j que iniciara en la posicion despues de la posicion i
        for j in range(i+1, len(lista)):
            #Si la posicion j es menor que la posicion menor o se actualizara j como el nuevo numero menor de la lista
            if lista[j] < lista[menor]:
                menor = j
        #Se intercambian posiciones entre i y el numero menor
        lista[i], lista[menor] = lista[menor], lista[i]

        #Se imprime el estado de la lista
        print(f'pasada #{i+1}', lista)

def insertion_sort(lista): #Funcion para ordenar una lista utilizando la estructura de ordenamiento por insercion
    #Ciclo For para ir recorriendo la lista desde la segunda posicion hasta el final de la lista
    for i in range(1,len(lista)):
        save = lista[i] #Variable creada para no perder el valor que se va a comparar
        index = i #Variable creada para no modificar el vlaor de i
        #Ciclo while que solo se activara cuando no se llegue a 0 y que la posicion anterior al indice sea mayor que la actual
        while index > 0 and lista[index-1] > save:
            #Se cambia el valor de la primera posicion con la posicion anterior
            lista[index] = lista[index-1]
            print(lista)
            index -= 1
        #Se actualiza la ultima posicion que tomo el index con el valor de la variable que se guardo
        lista[index] = save
        print(f'Ciclo #:{i}', lista)

def quick_sort(lista, l, r): #Funcion para ordenar una lista utilizando la estructura de ordenamiento rapido
    #Si la lista tiene un tamano mayor a 2
    if l < r:
        #El pivote sera el valor que partition_quick_sort regrese
        pivot = partition_quick_sort(lista, l, r)
        #Se imprime el pivote y las correspondientes sublistas
        print(f'{lista[l:pivot]}---Pivote: {lista[pivot]}----{lista[pivot+1:r+1]}')
        #Se vuelve a llamar la funcion de manera recursiva con los valores mayores e inferiores pero sin mover la posicion del pivote
        quick_sort(lista, l, pivot-1)
        quick_sort(lista, pivot+1, r)
#   ^^^^ juntos vvvv
def partition_quick_sort(lista,l,r): #Funcion que establece un numero en su posicion final
    #primer indice i que se encargara de buscar valores mayores al pivote
    i = l
    #segundo indice j que se encargara de buscar valores menores al pivote
    j = r - 1
    #Pivote sera el valor final de la lista
    pivot = lista[r]
    #mientras i y j no se crucen
    while i < j:
        #mientras i no llega al extremo final y el valor en la posicion i es menor a la del pivote
        while i < r and lista[i] < pivot:
            #i avanzara una posicion
            i +=1
        #mientras j no llegue al extremo izquierdo y el valor de la lista en la posicion j sea mayor a la del pivote
        while j > l and lista[j] >= pivot:
            #j retrocedera en 1
            j -= 1
        #Si i y j se cruzan se intercambiaran los valores de las posiciones
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]
    #Si el valor en la posicion i es mayor a la del pivote se intercambiaran las posiciones de el valor en el extremo derecho con los del indice i
    if lista[i] > pivot:
        lista[i], lista[r] = lista[r], lista[i]
    #Se regresa i como el valor que consiguio su ultima posicion.
    return i

def merge_sort(lista,cuenta): #funcion para ordenas una lista de datos utilizando la estructura de ordenamiento por mezcla
    #La funcion solo funcionara cuando sea llamada con una lista con mas de un dato
    if len(lista) > 1:
        #Se crean dos listas del inicio al medio y del medio  al final
        lista_izquierda = lista[:len(lista)//2]
        lista_derecha = lista[len(lista)//2:]
        print(f'lista: {lista} l:{lista_izquierda}, r:{lista_derecha}')

        #Recursivamente la funcion con las sublistas creadas
        merge_sort(lista_izquierda,cuenta)
        merge_sort(lista_derecha,cuenta)

        #se crea i el indice para la sublista de la izquierda, j para la derecha y k para la lista original
        i = j = k = 0
        #Mientras los indices no sean mayores al tamano de las listas
        while i <len(lista_izquierda) and j <len(lista_derecha):
            #Si el valor de la lista es izquierda al valor de la lista derecha el valor de la izquierda sera acomodado en la lista original
            if lista_izquierda[i] <= lista_derecha[j]:
                lista[k] = lista_izquierda[i]
                i += 1 #Indice de la izquierda aumenta en uno
            #De no ser asi el valor de la derecha se acomodara en la lista original
            else:
                lista[k] = lista_derecha[j]
                j += 1 #Indice de la derecha avanzara en uno
                #print(f'Cambio: {lista[k]}<{lista_izquierda[i]}')
                cuenta.aumenta()
            k += 1 #El indice de la lista avanzara cada vez que se cumpla un ciclo

        #Cuando solo se cumpla que el indice izquierdo sea menor al tamano de la lista
        while i < len(lista_izquierda):
            #se llenara la lista original con los valores restantes
            lista[k] = lista_izquierda[i]
            #ambos contadores avanzan
            i += 1
            k += 1

        #Cuando solo se cumpla que el indice derecho sea menor al tamano de la lista
        while j < len(lista_izquierda):
            #se llenara la lista original con los valores restantes
            lista[k] = lista_derecha[j]
            #ambos contadores avanzan
            j += 1
            k += 1

def shell_sort(lista):
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
        #Se establece flag como verdadero
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
                    print(f'#{j}: {lista} con gap de:{inte}')
                    #j avanza en 1 y band vuelve a True si se cumple la condicion para que se repita el ciclo
                    j= j+1
                    flag = True
                #i avanza una posicion
                i = i+1
                #la posicion ira avanzando de 1 en 1

def heap_sort(a,cuenta):  # Funcion heapsort que funciona al enviar un arreglo como parametro

    # Se llama la funcion heapify con el arreglo a y la cantidad de elementos en el arreglo como parametros
    heapify(a, len(a),cuenta)
    # Se establece end como la posicion final del arreglo a
    end = len(a) - 1

    # Ciclo while que acabara hasta que end llegue a 0
    while end > 0:
        # Se intercambian las posiciones del primer y ultimo numero del arreglo a
        a[end], a[0] = a[0], a[end]
        # end disminuye en 1 cada vez que se cumple un ciclo
        end -= 1
        # Se llama la funcion sift_down con la lista modificada, 0, y la variable end como parametros
        shift_down(a, 0, end,cuenta)

    # Por ultimo el metodo ordenara la lista
# ^^^^ juntos vvvv
def heapify(a, count,cuenta):  # Funcion heapify que empieza a trabajar cuando recibe una lista y la extencion de esta
    # Se crea la variable start que sera igual al redondeo de la posicion final menos 1 y dividido entre 2
    start = int((count - 2) / 2)
    # Se imprime el valor de start para indicar cual fue la posicion inicial que se tomo
    print('posicion inicial', start)
    # Ciclo while que acabara hasta que start llegue a 0
    while start >= 0:
        # Se llama la funcion sift_down con la lista, la variable start y la ultima posicion del arreglo como parametros
        shift_down(a, start, count - 1,cuenta)
        # Start disminuira en 1 cada vez que se cumple un ciclo
        start -= 1
# ^^^^ juntos vvvv
def shift_down(a, start, end, cuenta):  # Funcion heapify que empieza a trabajar cuando recibe una lista, un inicio y un final
    # Root funciona como la raiz de nuestro arbol y es igualada con la posicion inicial
    root = start
    # Mientras la posicion del hijo sea menor o igual que la ultima posicion de la lista final
    while (root * 2 + 1) <= end:
        # La variable child funciona como las posicion hijo de la raiz y esta es la posicion de la raiz + 1 debido a que en python se inicia con la posicion 0 se ocupa el +1
        child = root * 2 + 1
        # Se declara la posicion swap que funcionara como un auxiluar y esetara igualada a la posicion raiz
        swap = root
        # Si el valor de a en la posicion swap (que puede ser child, child +1 o root) es menor al valor de a en la posicion child swap cambia su valor al de child
        if a[swap] < a[child]:
            swap = child
        # Si child + 1 (hijo 2) es menor a la ultima posicion del arreglo y el valor de del arreglo a en swap es menor al valor de a en el hijo 2  swap adaptara el valor del hijo 2
        if (child + 1) <= end and a[swap] < a[child + 1]:
            swap = child + 1
        # Si swap es distinto al valor de root (si se cumplio alguna de las otras 2 condiciones) se intercambian los valores en la posicion root con el de la posicion swap
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            cuenta.aumenta()
            print(f'#{cuenta.numero} {a}')
            # la nueva raiz sera el valor que swap adopto
            root = swap
        # En caso de no cumplirse ningun if anterior, el ciclo continuara
        else:
            return
        # Se imprime como queda la lista despues de cada corrida de esta funcion cuando es llamada por el while de la funcion heapify

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
            print(f'Se encontro {numero} en la posicion [del arreglo]: {medio}, por lo que hay {medio} numeros detras de el...')
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
        print(medio)
        print('WOOPS!...Parece que el valor no se encuentra dentro del arreglo..intente de nuevo......')

class Pila:
    # Se crea el constructor con la variable tamano como variable
    def __init__(self, tamano):
        # Self. tamano sera usado para referenciar la cantidad de elementos en la lista
        self.tamano = tamano
        # Se muestra la lista iniciando en un arreglo vacio
        self.lista = []
        # Se inicia self.top para saber la ultima posicion del arreglo
        self.top = -1

    # Metodo para determinar si la lista esta vacia
    def esta_vacia(self):
        # En caso de que el top no haya avanzado la lista estara vacia
        if self.top == -1:
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para determinar si la lista esta llena
    def esta_llena(self):
        # En caso de que el top sea igual que la ultima posicion la lista estara llena
        if self.top == (self.tamano - 1):
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para insertar un valor
    def insertar(self, item):
        if self.esta_llena() == False:
            # Se agrega el valor deseado en la ultima posicion
            self.lista.append(item)
            # Top aumentara en 1 indicando la ultima posicion de la lista
            self.top += 1
        else:
            # print('La pila esta llena...')
            return False

    # Metodo para extraer un valor
    def extraer(self):
        # Si la lista esta vacia no se extrae ningun valor
        if self.esta_vacia() == True:
            print('La pila esta vacia...')
            return False
        # Si contiene un valor se extrae el ultimo que fue agregado
        else:
            # Se saca el ultimo de la fila
            save = self.lista.pop(self.top)
            # Se guarda el valor extraido en caso de ser necesario
            self.top -= 1
        # Se regresa el valor guardado
        return save

    # Metodo para identificar el valor maximo en la lista
    def max(self):
        # Si la lista esta vacia se imprimira un mensaje diciendo que no hay valor maximo
        if self.esta_vacia() == True:
            print('La pila esta vacia y por ello no hay valor maximo...')
            return False
        # Si no es asi por medio de un for se ira comparando la posicion 0 actualizando la variable mayor cada vez que se encuentre un valor mayor al de la posicion 0
        else:
            mayor = self.lista[0]
            for i in range(self.top + 1):
                if self.lista[i] > mayor:
                    mayor = self.lista[i]
            # Se regresa e imprimer el numero identificado como el mayor
            print(mayor)
            return mayor

class Cola:
    # Se crea el constructor con la variable tamano como variable
    def __init__(self, tamano):
        # Self. tamano sera usado para referenciar la cantidad de elementos en la lista
        self.tamano = tamano
        # Se muestra la lista iniciando en un arreglo vacio
        self.lista = []
        # Se inicia self.top para saber la ultima posicion del arreglo
        self.top = -1

    # Metodo para determinar si la lista esta vacia
    def esta_vacia(self):
        # En caso de que el top no haya avanzado la lista estara vacia
        if self.top == -1:
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para determinar si la lista esta llena
    def esta_llena(self):
        # En caso de que el top sea igual que la ultima posicion la lista estara llena
        if self.top == (self.tamano - 1):
            return True
        # De lo contrrario no lo estara
        else:
            return False

    # Metodo para insertar un valor
    def inserar(self, item):
        if self.esta_llena() == False:
            # Se agrega e; valor deseado en la ultima posicion
            self.lista.append(item)
            # Top aumentara en 1 indicando la ultima posicion de la lista
            self.top += 1
        else:
            # print('La pila esta llena...')
            return False

    # Metodo para extraer un valor
    def extraer(self):
        # Si la lista esta vacia no se extrae ningun valor
        if self.esta_vacia() == True:
            # print('La pila esta vacia...')
            return False
        # Si contiene un valor se extrae el ultimo que fue agregado
        else:
            # Se saca el ultimo de la fila
            save = self.lista.pop(0)
            # Se guarda el valor extraido en caso de ser necesario
            self.top -= 1
        #Se regresa el valor guardado
        return save

class Contador:
    def __init__(self,inicio =0):
        self.numero = inicio
    def aumenta(self):
        self.numero += 1

    def imprime(self):
        print(f'Numero de intentos: {self.numero}')

def palindromos(palabra): #Funcion para determinar si una palabra es palindromo
    n = int(len(palabra))
    if n > 150:
        print('ERROR!.... Palabra con mas de 15 letras...')
    else:
        # Se crea la pila a
        a = Pila(n)
        # Ciclo for para copiar las letras de la palabra en la pila
        for i in range(n):
            a.insertar(palabra[i])
        # Variables j para comprobar que las letras sean iguales
        j = False
        # j_2 sera True desde un inicio hasta que haya una diferencia en letras, esta sirve para evitar que palabras que solo comparten las letras del centro sean detectadas como palindromos
        j_2 = True
        # Ciclo for para ir comparando la primer letra con la ultima
        i = 0
        while i < (n // 2):
            # Si son iguales
            save = str(a.extraer())
            #ciclos while para evitar las comparaciones entre letras y espacios
            while save == ' ':
                save = str(a.extraer())
            if a.lista[i] == ' ':
                flag = True
                while flag == True:
                    i += 1
                    if a.lista[i] != ' ':
                        flag = False

            if save == str(a.lista[i]) or save.upper() == str(a.lista[i]) or save == str(a.lista[i]).upper():
                # J sera verdadera
                j = True
            else:
                # Si no, ambas seran negativas
                j = False
                j_2 = False
            i+= 1


        # Si ambas j son verdaderas la palabra es palindromo
        if j == True and j_2 == True:
            print('La palabra es palindromo!!')
        # Si j no es verdadero la palabra no es palindromo
        else:
            print('La palabra no es palindromo...')

def ordenes():
    # Se llama el metodo para pedir un numero para pedir el numero de instrucciones que se van a usar
    n = ask_for_integer('')

    # Ciclo while para validar que el numero no sea ni mayor a 400,000 ni menor a 1 como indican las instrucciones
    while n < 1 or n > 400000:
        n = ask_for_integer('ERROR!...... el numero debe estar en un rango de 1 a 400,000...Digite de nuevo: ')
    # Se crea el objeto lista que pertenecera a la clase Pila con el numero de instrucciones como parametro
    lista = Pila(n)

    # Se crea el objeto ordenes que pertenecera a la clase Cola con el numero de instrucciones como parametro
    ordenes = Cola(n)

    # contador i para el segundo ciclo while que no acabara hasta que llegue al numero de instrucciones sea alcanzado
    i = 0
    while i < n:
        # Se crea la entrada orden que recibira lo que el usuario teclee
        orden = input('')

        # Si las primeras 4 letras son "push" se cumplira
        if orden[:4] == 'push':
            # Cuando la funcion validar_int regrese un False el contador retrocera en 1
            if validar_int(orden[4:], 'push') == False:
                i -= 1
            # Si la misma funcion regresa un numero que no este dentro de [0-105] se regresara la cuenta e imprimira un mensaje de que no es valido
            elif int(orden[4:]) < 0 or int(orden[4:]) > 105:
                print('INVALIDO:.. No digitar un numero mayor a 105 ni menor a 0...')
                i -= 1
            # Si pasa los 2 flintros se enviara lo tecleado como parametro a la cola ordenes
            else:
                ordenes.inserar(orden)

        # Si se digita max o pop
        elif orden == 'max' or orden == 'pop':
            # Si es lo primero que se teclea enviara un mensaje diciendo que la pila se encuentra vacia y la cuenta no avanzara
            if i <= 0:
                print('Opcion no valida... la pila se encuentra vacia')
                i -= 1
            # Si pasa el filtro anterior se manda lo escrito como parametro a la cola
            else:
                ordenes.inserar(orden)
        # Si no se digita ninguna de las opciones la cuenta no avanzara
        else:
            print('Opcion no valida... digita de nuevo...')
            i -= 1
        i += 1

    # print(ordenes.lista)

    # Ciclo for para ejecutar las ordenes dadas en la cola
    for j in range(n):
        # Orden sera el valor extraido de la cola cuando se llama el metodo extraer
        orden = ordenes.extraer()

        # Si los primeros 4 cuaracteres son 'push' se llamara el metodo insertar con el numero que va despues del push
        if orden[:4] == 'push':

            lista.insertar(int(orden[4:]))

        # Si orden es igual a max se llama el metodo max que imprimira cual es el valor maximo de la lista
        elif orden == 'max':
            lista.max()

        # Si los caracteres del orden son igual pop se llamara el metodo extraer
        elif orden == 'pop':
            lista.extraer()

    # Finalmente se imprimira la lista
    print(lista.lista)

if __name__ == '__main__':
     #lista= [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]
     #busqueda_binaria(lista, 52)
     A = [15,67,8,16,44,27,12,35]

     insertion_sort(A)