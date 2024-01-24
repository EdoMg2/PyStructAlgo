#Meta 2.2 Lista circular doble.
#Hacer un programa que cumpla con las instrucciones de la Meta 2.2
#33069-EDUARDO MENDOZA GOMEZ

class Node:
#Se inicia la clase para los nodos
    def __init__(self, valor=None, next= None, prev=None):
        self.data = valor #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.next = next #Se establece que el siguiente del nodo sera None en un princiipio
        self.prev = prev #Se esstablece que el anterior del nodo sera none en un principio

    def getData(self):
        return self.data

class Circular_LinkedList:
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
        for i in range(self.size): #Ciclo for que terminara hasta que la lista sea recorrida
            if itr == self.last: #Si itr llega al ultimo nodo
                lista += str(itr.data) #Se agregarta el ultimo valor sin la flecha
            else: #Si no
                lista += str(itr.data) + ',' #Se agregara el siguiente valor con la flecha pauntando al siguiente numero
            itr = itr.next
        #Se imprime la lista
        print(lista)

    def getVacio(self): #Metodo que regreserara un True cuando la lista se encuentre vacia
        if self.first == None: #Si no hay un primer valor, se devolvera un True
            return True

    def insertar_inicio(self,data): #Metodo para insertar un dato al inicio de la lista
        node = Node(data) #se crea un nodo con el dato que se le pasa al llamar el metodo

        if self.getVacio()== True: #Si la lista esta vacia, se le asiganra el nodo creado al primer y ultimo valor de la lista
            self.first = self.last = node
        else: #Cuando no esta vacia
            self.first.prev = node #el anterior primer nodo hacia atras apuntara al nodo anterior creado
            node.next = self.first #El siguiente nodo del nodo creado sera el que anteriormente sera el primero
            node.prev = self.last #El previo al nodo creado sera el ultimo valor de la lista
            self.first = node #Se establece el primer nodo de la lista como el nodo creado
            # Se actualizan el previo y ultimo del ultimo y primer nodo de la lista
            self.first.prev = self.last
            self.last.next = self.first

        self.size += 1 #El tamano aumentara en 1
        return

    def insertar_final(self, data): #Metodo para insertar un dato al final de la lista
        node = Node(data) #se crea un nodo con el dato que se le pasa al llamar el metodo

        if self.getVacio() == True:  # Si la lista esta vacia, se le asiganra el nodo creado al primer y ultimo valor de la lista
            self.first = self.last = node
        else: #Cuando no esta vacia
            self.last.next = node #el siguiente elemento del anterior ultimo nodo sera el nodo creado
            #Se asignan el primer y ultimo nodos de la lista como el nodo previo y siguiente del nodo creado
            node.next = self.first
            node.prev = self.last
            self.last = node #Se establece el nodo creado como el ultimo nodo de la lista
            # Se actualizan el previo y ultimo del ultimo y primer nodo de la lista
            self.last.next = self.first
            self.first.prev = self.last
        self.size += 1 #El tamano aumentara en 1

    def extraer_inicio(self): #Metodo para extraer un elemento al inicio de la lista
        if self.getVacio()== True: #No se elimina nada de una lista vacia
            return
        #Si se quiere borrar un elemento de una lista con un elemento
        elif self.size == 1:
            self.first = self.last = None #Se deja vacia la lista
        #Si la lista contiene mas de un elemento
        else:
            #El primer nodo pasara a ser el siguiente del que anteriormente era el primero
            self.first = self.first.next
            # Se actualizan el previo y ultimo del ultimo y primer nodo de la lista
            self.last.next = self.first
            self.first.prev = self.last
        self.size -= 1 #El tamano de la lista disminuira en 1
        return

    def extraer_final(self): #Metodo para extraer un elemento al final de la lista
        if self.getVacio() == True:  # No se elimina nada de una lista vacia
            return
        # Si se quiere borrar un elemento de una lista con un elemento
        elif self.size == 1:
            self.first = self.last = None  # Se deja vacia la lista
        # Si la lista contiene mas de un elemento
        else:
            self.last = self.last.prev #Se actualiza el penultimo valor de la lista como el penultimo
            # Se actualizan el previo y ultimo del ultimo y primer nodo de la lista
            self.last.next = self.first
            self.first.prev = self.last
        self.size -= 1 #El tamano de la lista disminuira en 1
        return


if __name__ == '__main__':
    #Se crea l como una lista circularmente enlazada
    l  = Circular_LinkedList()
    #Cicloc for que agregara un elemento al principio y final de la lista en cada ciclo de cinco
    for i in range(5):
        l.insertar_inicio(i)
        l.insertar_final(i+10)
    #Se imprime la lista
    print('Se esta creando tu lista...')
    l.print()

    print('Se extraeran dos numeros del inicio...y el ultimo de la lista....')
    #A traves de los metodos se eliminaran los dos ultimos y el primer nodo de la lista,
    l.extraer_inicio()
    l.extraer_inicio()
    l.extraer_final()
    #Se imprime la lista
    l.print()

    #variable para recorrer toda la lista
    itr = l.first
    print(' n:Previo  N  Siguiente')
    for i in range(l.size): #Por medio de un for se recorrera toda la lista

        #Se imprimira el nodo junto al nodo previo y siguiente a los que apunta
        print(f'#{i+1}: {itr.prev.data} -- {itr.data} -- {itr.next.data}')
        itr = itr.next #Cada vez que se cumpla un for itr avanzara un elemento de la lista

# ULTIMA MODIFICACION 30 DE SEPTIEMBRE DEL 2021 A LAS 4:00 PM, TIJUANA BAJA CALIFORNIA