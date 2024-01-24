#Meta 2 1. listas enlazadas
#Realizar la clase lista enlazada de acuerdo a lo investigado y crear dentro del programa un ejemplo de su corrida
#33069-EDUARDO MENDOZA GOMEZ

class Node:
#Se inicia la clase para los nodos
    def __init__(self, valor=None, next= None):
        self.data = valor #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.next = next #Se establece que el siguiente del nodo sera None en un princiipio

class LinkedList: #Se crea la clase de listas enlazadas
    def __init__(self):
        self.first = None #Self.first funcionara como el primer elemento en la lista creada

    def print(self): #Metodo para imprimir la lista
        if self.first is None: #Si la lista se encuentra vacia, se imprimira un mensaje de error
            print("La lista enlazada se encuentra vacia")
            return
        #Si no esta vacia, la lista se imprimira con sus valores en orden con una flecha '--->' entre cada uno.
        itr = self.first #Valor que sera introducido en el str vacio 'lista'
        lista = '' #cadena vacia que se ira llenando con cada valor que contenga la clase
        while itr:
            lista += str(itr.data)+' --> ' if itr.next else str(itr.data) #Se agregan los valores que tenga la clase guardados
            itr = itr.next
        #Se imprime la lista
        print(lista)

    def size(self): #Metodo para conseguir el tamano de la lista
        cuenta = 0 #Se crea un contador que iniciara en 0
        itr = self.first #variable igualada al primer valor de la lista
        #Ciclo while que acabara hasta que itr sea igual a None
        while itr:
            #el contador aumentara en 1 cada vez que haya un nodo despues del contado
            cuenta+=1
            #itr sera el siguiente nodo del que con el inicio en el ciclo while
            itr = itr.next
        #se regresa el contador
        return cuenta

    def insertar_inicio(self, data): #Metodo para ingresar un elemento al inicio de la lista
        node = Node(data, self.first) #se crea un nodo con el valor que anteriormente era el primero como posicion y el valor que se decida enviar como parametro
        self.first = node #El primer valor en la lista sera el nodo creado

    def insertar_final(self, data): #Metodo para ingresar un elemento al final de la lista
        if self.first is None: #si la lista se encuentra vacia
            self.first = Node(data, None) #el ultimo elemento sera el primero en consecuencia
            return
        #si no es asi se crea un itr igualado al primer elemento de la lista
        itr = self.first

        #por el ciclo while se busca la ultima posicion de la lista haciendo que el cicclo acabe cuando no haya un itr.next
        while itr.next:
            itr = itr.next
        #Se crea un nodo con el valor dado como parametro en la posicion final que fue buscada por el ciclo while anterior
        itr.next = Node(data, None)


    def insertar_en(self, posicion, data): #Metodo para insertar un valor en una posicion deseada con posicion y data como parametros deseados
        if posicion<0 or posicion>self.size(): #if para prevenir que se de una posicion que no este dentro de las dimensiones de la lista
            raise Exception("Posicion no valida....") #se imprime un mensaje
        #Si se da la posicion 0 se manda a llamar el metodo insertar_inicio con el valor dado como parametro
        if posicion==0:
            self.insertar_inicio(data)
            return

        #contador que iniciara en 0 para encontrar la posicion deseada
        cuenta = 0
        itr = self.first #variable que se igualara al primer elemento de la lista
        while itr: #ciclo while que avanzara hasta recorrer toda la lista
            if cuenta == posicion - 1: #Si el contador es igual a la posicion deseada menos 1, se creara un nodo con los valores y la posicion que se encuentran como parametros
                node = Node(data, itr.next)
                #El nisiguiente nodo del nodo en el que se encuentre el cilco while sera el nodo creado
                itr.next = node
                break #Se acaba el ciclo while
            #itr y la cuenta avanzara una posicion
            itr = itr.next
            cuenta += 1

    def remover_en(self, posicion): #Metodo para remover un valor de la lista en una posicion deseada
        if posicion<0 or posicion>=self.size(): #if para prevenir que se de una posicion que no este dentro de las dimensiones de la lista
            raise Exception("Posicion no valida....")
        #Si la posicion mandada es 0, se eliminara el primer elementgo de la lista
        if posicion == 0:

            #El primer elemento sera el nodo que le sigue
            self.first = self.first.next
            return
        #Si se envia una posicion distinta al 0, se crearan las variables cuenta e itr
        cuenta = 0
        itr = self.first
        #Igual que en el metodo anterior se buscara la posicion anterior a la posicion deseada por medio de un ciclo while
        while itr:
            #Si se cumple lo deseado se eliminara el valor de la posicion deseada de la misma forma que se logro cuando se envia la posicion 0.
            if cuenta == posicion - 1:
                itr.next = itr.next.next
                break
            #itr y cuenta avanzaran en 1 con cada ciclo while
            itr = itr.next
            cuenta += 1


    def insertar_valores(self, data_list): #Metodo para insertar mas de un valor por medio de un arreglo como parameto
        self.first = None #se establece, que no habra un primer nodo

        #Ciclo for parfa ir agregando cada elemento del arreglo en el orden dado
        for data in data_list:
            self.insertar_final(data)

    def buscar_posicion(self, data): #Metodo para buscar la posicion por medio de un valor dado
        #Se crean cuentra e itr como variables auxiliares
        cuenta = 0
        itr = self.first
        #Ciclo while que recorrera todos los elemntos de la lista
        while itr:
            #si el valor de itr es igual al parametro que se quiere enviar
            if itr.data == data:
                #se regreserara cuenta como la posicion en la que se encuentra el valor buscado
                return cuenta
            #Se actualizan itr y cuenta a la siguiente posicion
            itr = itr.next
            cuenta += 1
        #Si no se encontro el valor se imprimira un mensaje
        print('Valor enviado no se encuentra en la lista....')

    def buscar_valor(self, posicion):
        if posicion<0 or posicion>=self.size(): #if para prevenir que se de una posicion que no este dentro de las dimensiones de la lista
            raise Exception("Posicion no valida....")
        # Se crean cuentra e itr como variables auxiliares
        cuenta = 0
        itr = self.first
        # Ciclo while que recorrera todos los elemntos de la lista
        while itr:
            # si el valor de itr es igual al parametro que se quiere enviar
            if posicion == cuenta:
                #se regresa el valor de la posicion buscada
                return itr.data
            # Se actualizan itr y cuenta a la siguiente posicion
            itr = itr.next
            cuenta += 1

if __name__ == '__main__':
    milista = LinkedList() #Se crea el objeto mi lista que correspondera a la clase lista enlazada
    for i in range (10):
        #Se agrega a la lista los primeros 10 numeros del 0 al 9
        milista.insertar_final(i)
    print('Tu lista enlazada es: ')
    #Se imprime la lista
    milista.print()
    print('Se ha ingresado 90 en la ultima posicion...')
    #Se ingresa el numero 90 en la ultima posicion
    milista.insertar_final(90)
    milista.print()
    print('Se removera la posicion 4 que corresponde al numero 4')
    #SE remueve el valor que se encuentra en la posicion 4
    milista.remover_en(4)
    milista.print()
    print('El numero 777 se ha colocado en la posicion  numero 5...')
    #Se ingresa el valor 777 en la posicion numero 5
    milista.insertar_en(5, 777)
    milista.print()
    #Se imprime la posicion y valor que los metodos buscar_posicion y buscar_valor devuelven al ser ingresados
    print(f'La posicion del numero 9 es: {milista.buscar_posicion(9)}')
    print(f'El numero que se encuentra en la posicion numero 4 es: {milista.buscar_valor(4)}')
    milista.insertar_inicio(4)
    milista.print()

# ULTIMA MODIFICACION 23 DE SEPTIEMBRE DEL 2021 A LAS 7:55 PM, TIJUANA BAJA CALIFORNIA
