#Practica 2.1 BST-Recorridos-busqueda
#Sube tu programa, de árbol binario, con el metodo de insertar, los 3 recorridos y la busqueda. No olvides insertar datos en tu corrida para mostrar que funcionan tus metodos.
#33069-EDUARDO MENDOZA GOMEZ

class Node: #Clase Nodos que se utilizara en la clase arbol
#Se inicia la clase para los nodos
    def __init__(self, data):
        self.data = data #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.papa = None #Atributo para apuntar al padre de un nodo
        self.left = None #Atributo para apuntar a un hijo izquierdo de un nodo
        self.right = None #Atributo para apuntar a un hijo derecho de un nodo
        self.is_root = False #Atributo para saber si es raiz
        # Atributos para saber si es hijo izquiero o derecho
        self.is_left = False
        self.is_right = False

    def getData(self): #Metodo para llamar al valor del nodo
        return self.data

class Binary_tri: #Clase para arboles binarios
    def __init__(self):
        self.root = None #Se establece los valores iniciales de la raiz y peso del arbol
        self.weight = 0

    def is_empty(self): #Metodo que devolvera un True si la lista se encuentra vacia
        if self.weight == 0:
            return True

    def add_node(self,data): #Metodo para anadir valores al arbol
        node = Node(data) #Se crea un nodo con el numero que sea enviado como parametro
        if self.is_empty() == True: #Se verifica que la lista se encuentre vacia

            # Si es asi, la raiz del arbol sera el nodo creado
            node.is_root = True
            self.root = node

        else: #Si no esta vacia
            (side, node_papa) = self.get_position(data) #Se crean las variables side, y node_papa a partir del metodo get_position

            if side == 'left': #Si el metodo devolvio un 'left' significara que el valor izquierdo de la posicion devuelta sera el nuevo nodo
                node_papa.left = node
                node.is_left = True #Se establece que el nodo creado es izquierda de otro
            else: #Si no devolvio left significara que se encuentra a la derecha
                node_papa.right = node #el nuevo nodo sera un hijo derecho de la posicion deseada
                node.is_right = True #Se establece que es un hijo derecho
            node.papa = node_papa #El padre del nuevo nodo sera la posicion devuelta
        self.weight += 1 #Al final del metodo, el arbol pesara uno mas

    def get_position(self,data): #metodo para conseguir la posicion en donde deberia el valor que se va a introducir
        itr = self.root
        while itr:
            prev = itr
            side = None
            if data <= itr.data : #si el valor que se compara es menor igual al que fue pasado como parametro
                itr = itr.left #itr pasara a ser al que apunta hacia la derecha
                side = 'left'
            else:
                itr = itr.right #itr pasara a ser al que apunta hacia la izquierda
                side = 'right'
        return (side, prev) #Se regresa prev como la posicion deseada y side la direccion a la que apunta

    def in_order(self,node): #Metodo para mostrar los valores del arbol de acuerdo al orden in order
        # i - r - d
        if node: #Si se llama cuando el nodo no es None
            self.in_order(node.left) #Se llama el metodo de nuevo pero con el hijo izquierdo
            print(node.data, end=" ") #Se imprime el valor del nodo
            self.in_order(node.right) #Se llama el metodo de nuevo pero con el hijo derecho

    def pos_order(self, node): #Metodo para mostrar los valores del arbol de acuerdo al orden pos order
        # i - d - r
        if node:
            self.pos_order(node.left) #Se llama el metodo de nuevo pero con el hijo izquierdo
            self.pos_order(node.right) #Se llama el metodo de nuevo pero con el hijo derecho
            print(node.data, end=" ") #Se imprime el valor del nodo

    def pre_order(self, node): #Metodo para mostrar los valores del arbol de acuerdo al orden pre order
        # r - i - d
        if node:
            print(node.data, end=" ") #Se imprime el valor del nodo
            self.pre_order(node.left) #Se llama el metodo de nuevo pero con el hijo izquierdo
            self.pre_order(node.right) #Se llama el metodo de nuevo pero con el hijo derecho

    def search(self, value, root):
        if self.is_empty() == True: #Si la lista se encuentra vacia, se imprimira un mensaje
            print('Arbol vacio')
            return
        else: #Si hay un elemento
            if value == root.data: #se busca saber si es igual que la raiz del arbol
                return root #Se regresa el nodo
            elif value <= root.data: #Si la raiz es es mayor que el valor que se busca, se volvera a llamar el metodo en forma recursiva con el primer hijo izquiero de la raiz
                return self.search(value,root.left)
            else: #De lo contrario se llamara de forma recursiva con el primer hijo derecho de la raiz
                return self.search(value, root.right)

    def delete(self, value): #Metodo de prueba
        deleted = self.search(value,self.root)
        if deleted:
            (child, direction) = self.has_offspring(deleted)
            if child == 0:
                if deleted.is_left == True:
                    deleted.papa.left = None
                    print('se borro izquierda')
                else:
                    deleted.papa.right = None
                    print('se borro derecha')
                deleted = None

            elif child == 1:
                print(direction)
                if deleted.is_left == True:
                    if direction == 'left':
                        deleted.papa.left = deleted.left
                        deleted.left.papa = deleted.papa
                    else:
                        deleted.papa.left = deleted.right
                        deleted.right.papa = deleted.papa
                        deleted.right.is_right = False
                        deleted.right.is_left = True

                else:
                    if direction == 'left':
                        deleted.papa.right = deleted.left
                        deleted.left.papa = deleted.papa
                        deleted.right.is_right = True
                        deleted.right.is_left = False
                    else:
                        deleted.papa.right = deleted.right
                        deleted.right.papa = deleted.papa
                deleted = None
            else:
                sucesor = self.sucesor(deleted)
                deleted.data = sucesor.data
                if sucesor.is_left == True:
                    sucesor.papa.left = None
                else:
                    sucesor.papa.right = None
                sucesor = None

    def sucesor(self, node):
        itr = node.left
        itr_2 = itr.right
        if itr.right:
            while itr_2.right:
                itr_2 = itr_2.right
            itr = itr_2
        print(f'se devolvera itr:{itr.data}')
        return itr




    def has_offspring(self, node):
        count = 0
        direction = None
        if node.right:
            count += 1
            direction = 'right'
        if node.left:
            count += 1
            direction = 'left'
        return count, direction



if __name__ == '__main__':
    Pino = Binary_tri() #Se crea el arbol binario pino
    datos = [18, 8, 6, 9, 22, 21, 20,43] #Arreglo 'datos' con los valores que se agregaran al artbol pino
    #Ciclo for para agregar todos las posiciones del arreglo datos al arbol Pino
    for i in datos:
        Pino.add_node(i) #Se agrega cada posicion del arreglo al arbol

    #Se llaman los metodos y se imprimen en pantalla
    print('**RECORRIDA DEL ARBOL**\n')
    Pino.in_order(Pino.root)
    print('<--- Recorrida "en orden"')
    Pino.pos_order(Pino.root)
    print('<--- Recorrida "pos orden"')
    Pino.pre_order(Pino.root)
    print('<--- Recorrida "pre orden"')

    print('\n**BUSQUEDA***\n')
    #Se usa el metodo search y el valor que regresa se le asignara a la variable busqueda
    busqueda = Pino.search(22, Pino.root)
    #Se imprime el valor de la posicion buscada
    print(f'En la posicion: {busqueda}, se encuentra el numero {busqueda.data}, de tal forma que su rama quedaria:')
    print(f' {busqueda.papa.data} --> padre')
    print(f'   \ ')
    print(f'   {busqueda.data} --> hijo (posicion buscada)  ')
    print(f' /   \  ')
    print(f'{busqueda.left.data}   {busqueda.right.data} --> nietos/hijos ')

    # ULTIMA MODIFICACION 7 DE OCTUBRE DEL 2021 A LAS 14:50 PM, TIJUANA BAJA CALIFORNIA
