class Node:
#Se inicia la clase para los nodos
    def __init__(self, valor=None, next= None, prev=None):
        self.data = valor #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.next = next #Se establece que el siguiente del nodo sera None en un princiipio
        self.prev = prev #Se esstablece que el anterior del nodo sera none en un principio

    def getData(self):
        return self.data

class Doubly_LinkedList:
    def __init__(self):
        self.first = None #Self.first funcionara como el primer elemento en la lista creada
        self.last = None #Self.last  funcionara como el ultimo elemento en la lista creada
        self.size = 0 #Se establece el tamano como un atributo que iniciara en 0

    def print(self): #Metodo para imprimir la lista
        if self.first is None: #Si la lista se encuentra vacia, se imprimira un mensaje de error
            print("None <--> None")
            return
        #Si no esta vacia, la lista se imprimira con sus valores en orden con una flecha '--->' entre cada uno.
        itr = self.first #Valor que sera introducido en el str vacio 'lista'
        lista = '' #cadena vacia que se ira llenando con cada valor que contenga la clase
        while itr:
            lista += str(itr.data)+' <--> ' if itr.next else str(itr.data) #Se agregan los valores que tenga la clase guardados
            itr = itr.next
        #Se imprime la lista
        print(lista)

    def getVacio(self): #Metodo que regreserara un True cuando la lista se encuentre vacia
        if self.first == None:
            return True

    def insertar_inicio(self,data): #Metodo para insertar un dato al inicio de la lista
        node = Node(data) #se crea un nodo con el dato que se le pasa al llamar el metodo

        if self.getVacio()== True: #Si la lista esta vacia, se le asiganra el nodo creado al primer y ultimo valor de la lista
            self.first = self.last = node
        else: #Cuando no esta vacia
            node.next = self.first #el siguiente valor del nodo sera el que antes era el primero
            self.first.prev = node #El valor anterior al primer anterior sera el nodo creado
            self.first = node #el nuevo primer dato sera el nodo creado

        self.size += 1 #El tamano aumentara en 1

    def insertar_final(self, data): #Metodo para insertar un dato al final de la lista
        node = Node(data) #se crea un nodo con el dato que se le pasa al llamar el metodo

        if self.getVacio() == True: #Si la lista esta vacia, se le asiganra el nodo creado al primer y ultimo valor de la lista
            self.first = self.last = node
        else: #Cuando no esta vacia
            node.prev = self.last #El nodo anterior al nodo creado sera el que antes era el ultimo
            self.last.next = node #El siguiente al ultimo nodo sera el nodo creado
            self.last = node #se especifica que el ultimo sera el nodo creado

        self.size += 1 #El tamano aumentara en 1

    def insertar_en(self,data, index): #Metodo para agregar un dato een la posicion que se especifiquee como la variable index
        node = Node(data) #Se crea un nodo con el valor enviado como parametro
        if self.getVacio() == True: #Si la lista esta vacia se imprime un mensaje y se agregara el valor a la ultima posicion
            print('La lista se encuentra vacia, por lo que se ingresara en la unica posicion')
            self.first = self.last = node
            return
        elif self.size < index: #Si el tamano de la lista es menor a la posicion deseada se imprimira un mensaje para preguntar si se desea agregar en la ultima posicion
            pregunta = input('Introduciste una posicion mayor al tamaño de tu lista, presiona X si deseas agregarlo al final de la lista: ')
            if pregunta == 'x' or pregunta == 'X': #Si se introduce X o x se entiende que que se quera agregar al ultimo, por lo que se llamara el metodo anterior
                self.insertar_final(data)
                return
            else: #Si no se quiere, se acaba el metodo si agregar el elemento
                return
        elif self.size+1 == index: #Si se da una posicion que corresponderia a la ultima de la lista se llama el metodo correspondiente
            self.insertar_final(data)
            return
        elif index == 0 or index==1: #Si se da una posicion que da a endender que se quiere agregar al inicio se llama al metodo correspondiente
            self.insertar_inicio(data)
            return
        else: #si no significa que se quiere agregar en una posicion especifica
            cuenta = 1 #Se crea un contador que iniciara en 1
            itr = self.first #Se crea itr que sera el nodo que ira recorriendo toda la lista, pero iniciara en el primero
            while itr: #Se recorre la lista hasta llegar el none
                # Si la cuenta llega a la posicion que se envio como parametro
                if cuenta == index:
                    #Se colocan las nuevas posiciones posicionando el nodo creado en la posicion que estaba el itr
                    node.next = itr
                    node.prev = itr.prev
                    #Se especifica que el nodo sera el siguiente al anterior del que se esta sustituyendop
                    itr.prev.next = node
                    itr.prev = node

                    self.size += 1 #El tamano aumentara en 1

                    break #se rompe el while
                # itr y cuenta avanzaran en 1 con cada ciclo while
                itr = itr.next
                cuenta += 1

    def extraer_inicio(self): #Metodo para extraer un elemento al inicio de la lista
        if self.getVacio()== True: #No se elimina nada de una lista vacia
            return
        #si no es asi se crea un itr igualado al primer elemento de la lista
        else:
            aux = self.first
            self.first = self.first.next #Se ajusta a que el primer valor sea el que anteriormente era el segundo
            self.first.prev = None #Se elimina el valor anterior guardado del nuevo primer elemetno
            self.size -= 1
            aux = None
            return

    def extraer_final(self): #Metodo para extraer un elemento al final de la lista
        if self.getVacio()== True: #No se elimina nada de una lista vacia
            return
        # si no es asi se crea un itr igualado al primer elemento de la lista
        else:
            aux = self.last
            self.last = self.last.prev #Se actualiza el penultimo valor de la lista como el penultimo
            self.last.next= None #Se actualiza que el valor al que apunte sea None
            self.size -= 1 #El tamano de la lista disminuye
            aux = None
            return

    def extraer_en(self, index):
        if self.getVacio() == True: #Si la lista esta vacia no se hace nada
            return

        elif self.size < index: #Si el tamano de la lista es menor a la posicion deseada se imprimira un mensaje para preguntar si se desea agregar en la ultima posicion
            pregunta = input('Introduciste una posicion mayor al tamaño de tu lista, presiona X si deseas extraer al final de la lista: ')
            if pregunta == 'x' or pregunta == 'X': #Si se introduce X o x se entiende que que se quera agregar al ultimo, por lo que se llamara el metodo anterior
                self.extraer_final()
                return
            else: #Si no se quiere, se acaba el metodo sin extraer el elemento
                return
        elif self.size == index: #Si se da una posicion que corresponderia a la ultima de la lista se llama el metodo correspondiente
            self.extraer_final()
            return
        elif index == 0 or index==1: #Si se da una posicion que da a endender que se quiere extraer al inicio se llama al metodo correspondiente
            self.extraer_inicio()
            return
        else: #si no significa que se quiere agregar en una posicion especifica
            cuenta = 1 #Se crea un contador que iniciara en 1
            itr = self.first #Se crea itr que sera el nodo que ira recorriendo toda la lista, pero iniciara en el primero
            while itr: #Se recorre la lista hasta llegar el none
                # Si la cuenta llega a la posicion que se envio como parametro
                if cuenta == index:
                    aux = itr
                    itr.prev.next = itr.next #Se actualizan los indicadores anteriores y posteriores para asi eliminar la posicion que se busca eliminar
                    itr = itr.next #el valor que antes se encontraba en esa posicion ahora sera el que le seguia
                    itr.prev= itr.prev.prev #El valor previo de la nueva posicion sera el previo del previo
                    aux = None
                    self.size -= 1 #El tamano disminuye en 1


                    break #se rompe el while
                # itr y cuenta avanzaran en 1 con cada ciclo while
                itr = itr.next
                cuenta += 1

if __name__ == '__main__':

    lista = Doubly_LinkedList()
    lista.insertar_final(4)
    lista.insertar_inicio(43)
    lista.print()
    lista.insertar_final(8)
    lista.print()
    lista.insertar_en('prueba1', 3)
    lista.print()
    lista.insertar_en('prueba2', 2)
    lista.print()
    lista.extraer_en(1)
    lista.print()
    lista.extraer_en(3)
    lista.print()
    print(lista.last.prev.next.data)
