#Meta 1.5 :Proyecto Parcial 1 Implementación de Pilas.
#Crear un programa que sea capaz de informar cuando haya un error al usar los brackets (), {}, []
#33069-EDUARDO MENDOZA GOMEZ

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

def validar(lista): #Funcion creada para detectar los brackets dentro de una lista y validar que esten bien o mal escritos
    #Se crean las listas abierto con los brackets abiertos y cerrado con los brackets cerrados, asegurandose de que la posicion del abierto coincida con el del cerrado.
    abierto = ["[", "{", "("]
    cerrado = ["]", "}", ")"]
    #Se crea la pila stack con la Clase creada anteriormente
    stack = Pila(105)
    #Se define j=0 y funcionara como el contador del programa
    j = 0
    #Se inicia un ciclo for  que ira recorriendo todos los datos dentro de la lista a la que se le ingrese como parametro de la funcion
    for i in lista:
        #Cada vez que se cumpla el for j avanzara en 1
        j += 1
        if i in abierto: #Si el dato en el que se encuentra i es un bracket abierto
            #Se enviara el mismo valor a la pila stack
            stack.insertar(i)
        elif i in cerrado: #Si el dato es un bracket cerrado
            #Se creara la variable pos que sera la posicion en la que se encuentra ese bracket dentro del arreglo cerrado
            pos = cerrado.index(i)
            #Si no es el primer elemento dentro de stack,  es decir, ya se ha enviado un bracket abierto, y la posicion del cerrado coincide con la del abierto significara que se escribio correctamente
            if (stack.top > -1) and (abierto[pos] == stack.lista[stack.top]):
                #Se quita el bracket abierto que se envio a stack
                stack.extraer()
            #Si no, significara que se envio un bracket cerrado que no correspondia o que al abierto enviado o que el primer bracket que se envio es cerrado
            else:
                #Se regresa la posicion en que se encuentra el bracket cerrado
                return j
                break
    #Si al final el stack se encuentra vacio significara que la input fue escrita correctamente
    if stack.top == -1:
        #Se regresa un mensaje validando la input
        return "Success"
    #De lo contrario se regresa la ultima posicion
    else:
        return j

if __name__ == '__main__':
    #Se crea entrada que sera lo que el usuario quiera teclear
    entrada = input()
    #contador para determinar el numero real de caracteres dentro de la entrada sin contar los espacios
    largo = 0
    #Ciclo for para validar la verdadera cantidad de caracteres
    for i in range(len(entrada)):
        #Si el valor de la posicion que compara es igual a espacio largo no aumentara
        if entrada[i]==' ':
            largo= largo
        #Si no, significara es un caracter, por lo que largo aumentara en 1
        else:
            largo += 1

    #bucle while para evitar entradas con 0 o mas de 105 caracteres.
    while largo > 105 or largo  <1:
        largo = 0
        # Se vuelve a pedir la entrada
        entrada = input('ERROR... Solo introduzca cadenas con una cantidad de caracteres entre 105 y 1: ')
        #Se repite el ciclo for anterior
        for i in range(len(entrada)):
            if entrada[i] == ' ':
                largo = largo
            else:
                largo += 1

    #Se imprime el valor que validar regrese (La posicion del error o 'success'
    print(validar(entrada))

# ULTIMA MODIFICACION 18 DE SEPTIEMBRE DEL 2021 A LAS 5:45 PM, TIJUANA BAJA CALIFORNIA