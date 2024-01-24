#PRIMER EXAMEN PARCIAL ESTRUCTURA DE DATOS
#Hacer un programa que cumpla con las instrucciones del examen
#33069-EDUARDO MENDOZA GOMEZ

def validar_int (numero): #Funcion para validar que lo que se teclea sea un numero

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
            print(f'INVALIDO: Solo digite enteros...')
            # En todos los errores se regresa un False y se acaba la funcion
            return False
            break
        except SyntaxError:
            print(f'INVALIDO: Solo digite enteros...')

            return False
            break
        except NameError:
            print(f'INVALIDO: Solo digite enteros...')

            return False
            break

def lista_separada(separacion): #funcion para crear una lista a partir de un solo input
   #Se crea lista_inicial como lo que se va a digitar
   lista_inicial = input('')
   lista = lista_inicial.split(separacion) #por medio de .split se puede dividir el arreglo por espacios

    #Si la lista tiene un espacio al final sera eliminado por el metodo.pop
   if lista[len(lista)-1] == '':
       lista.pop(len(lista)-1)

    #ciclo for para validar que todos los datos sean numeros y que estos esten entre 1<= k <= 10^5
   for k in range(len(lista)):
       if validar_int(lista[k]) == False or validar_int(lista[k])> pow(10,5):
           return False

   #Condiciones if para cuando el valor del primer numero no sea igual al numero de numeros dados
   if int(lista[0]) < len(lista)-1:
       #Si se da un numero menor a  1 se iniciara un ciclo while que no parara hasta que se de una lista valida
       if int(lista[0]) < 1:
           while int(lista[0]) != len(lista) - 1:
               print('Numero de ordenes inferior a las especificaciones!...')
               lista_inicial = input('')
               lista = lista_inicial.split(separacion)
               if lista[len(lista) - 1] == '':
                   lista.pop(len(lista) - 1)
        #Si no es el anteiror significa quee el numero de indicaciones es menor a los numeros dados por lo que la lista se ajusta al numero correspondiente
       else:
           gap = (len(lista)-1) - int(lista[0])
           for j in range(gap):
               lista.pop(len(lista)-1)

    #Si se da un numero mayor al de las indicaciones o
   elif int(lista[0]) > len(lista)-1 or int(lista[0])>3*pow(10,4):
       while int(lista[0]) != len(lista)-1:
           print('Error menos numeros de los dados...intenta de nuevo')
           lista_inicial = input('')
           lista = lista_inicial.split(separacion)
           if lista[len(lista) - 1] == '':
               lista.pop(len(lista) - 1)

   a = Cola(10^5)
   for i in range(len(lista)):
       a.inserar(int(lista[i]))

   a.extraer()

   return a

def quick_sort(lista, l, r): #Funcion para ordenar una lista utilizando la estructura de ordenamiento rapido
    #Si la lista tiene un tamano mayor a 2
    if l < r:
        #El pivote sera el valor que partition_quick_sort regrese
        pivot = partition_quick_sort(lista, l, r)
        #Se vuelve a llamar la funcion de manera recursiva con los valores mayores e inferiores pero sin mover la posicion del pivote
        quick_sort(lista, l, pivot-1)
        quick_sort(lista, pivot+1, r)

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
        return -1

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

if __name__ == '__main__':

    #Se llama la funcion lista_separada que se encargara de devolver dos colas
    lista_a = lista_separada(' ')
    lista_b = lista_separada(' ')
    #Si en la lista se regresa un False significara que habia un valor que no era numero entero entre los datos dados
    if lista_a == False or lista_b == False:
        #Se imprimira un error y el programa no continuara
        print('ERROR... solo numeros enteros superiores a 1 e inferiores a 10^5 porfavor.. intente de nuevo')

    # Si pasa el filtro el programa se ejecuta
    else:
        #Se llama la funcion quick_sort para ordenar la primera lista
        quick_sort(lista_a.lista, 0, len(lista_a.lista)-1)
        #Se imprime la lista ordenada
        print(lista_a.lista)
        #Se crea una tercera cola para guardar las posiciones de los valores dados
        lista_c = Cola(10^5)
        #Ciclo for para ir buscando cada numero y guardar el valor que regrese busqueda_binaria cuando encuentre o no el numero
        for i in lista_b.lista:
            lista_c.inserar(busqueda_binaria(lista_a.lista,i))
        #Se imprime la cola con los valores dados
        print(lista_c.lista)

# ULTIMA MODIFICACION 13 DE SEPTIEMBRE DEL 2021 A LAS 11:50 AM, TIJUANA BAJA CALIFORNIA