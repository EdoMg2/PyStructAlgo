#EXAMEN PRACTICO 2
#Sigue las indicaciones del examen
#33069-EDUARDO MENDOZA GOMEZ

class Node: #Clase Nodos que se utilizara en la clase arbol
#Se inicia la clase para los nodos
    def __init__(self, data):
        self.data = data #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.papa = None #Atributo para apuntar al padre de un nodo
        self.left = None #Atributo para apuntar a un hijo izquierdo de un nodo
        self.right = None #Atributo para apuntar a un hijo derecho de un nodo
        self.is_root = False #Atributo para saber si es raiz
        self.height = 1 #atributo altura que siempre iniciara en uno
        # Atributos para saber si es hijo izquiero o derecho
        self.is_left = False
        self.is_right = False

    def getData(self): #Metodo para llamar al valor del nodo
        return self.data

    def display(self):  # Metodo para visualizar la descendencia de un nodo
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):  # Metodo auxiliar de display
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

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

    def delete(self, value): #Metodo para eliminar elemetos del arbol
        deleted = self.search(value,self.root) #Se crea el nodo deleted que sera eel nodo con el valor que se quiere borrar
        if deleted: #Si hay un nodo
            (child, direction) = self.has_offspring(deleted) #Se llama el metodo para saber si el tono tiene hijos, y si es asi se crean child y direction con los parametros devueltos
            if child == 0: #Si el nodo a borrar no tiene hijos
                if deleted.is_root == True:
                    self.root = None
                elif deleted.is_left == True: #Si es un hijo izquierdo
                    deleted.papa.left = None #El apuntador de su padre pasara a apuntar a nada
                    #print('se borro izquierda')
                else: #Si no sera un hijo derecho
                    deleted.papa.right = None #Lo mismo pero con un hijo derecho
                    #print('se borro derecha')

                print(f'***Se borro el nodo hoja: {deleted} con un atributo.data = {deleted.data}')
                deleted = None #el espeacio de memoria se elimina

            elif child == 1: #Si tiene un hijo
                if deleted.is_root == True: #Si se desea eliminar la raiz cuando solo tiene un hijo
                    self.root = self.root.left or self.root.right #La raiz pasara a ser su hijo a la izquierda o derecha
                    self.root.papa = None #El apuntador del papa pasara a ser nulo
                    self.root.is_right = False #Las banderas de la raiz pasaran a reacomodarse
                    self.root.is_left = False
                    self.root.is_root = True

                else:
                    if deleted.is_left == True: #Si el nodo a borrar es un hijo izquierdo
                        if direction == 'left': #Si el hijo es un hijo izquierdo
                            deleted.papa.left = deleted.left #Se reasignan los apuntadores del papa e hijo para eliminar el deseado
                            deleted.left.papa = deleted.papa
                        else: #Si no su hijo sera un hijo derecho
                            deleted.papa.left = deleted.right #Se reasignan los apuntadores del papa e hijo para eliminar el deseado
                            deleted.right.papa = deleted.papa
                            deleted.right.is_right = False #Las banderas cambian de acuerdo a su nueva posicion respecto a su padre
                            deleted.right.is_left = True

                    else: #Si no deleted es un hijo derecho
                        if direction == 'left': #Si el hijo es un hijo izquierdo
                            deleted.papa.right = deleted.left #Se reasignan los apuntadores del papa e hijo para eliminar el deseado
                            deleted.left.papa = deleted.papa
                            deleted.left.is_right = True  # Las banderas cambian de acuerdo a su nueva posicion respecto a su padre
                            deleted.left.is_left = False
                        else: #Si no el hijo es un hijo derecho
                            deleted.papa.right = deleted.right
                            deleted.right.papa = deleted.papa

                    print(f'***Se borro el nodo con un hijo: {deleted} con un atributo.data = {deleted.data}')
                    deleted = None #SE elimina el espacio de memoria de deleted

            else: #Si el nodo tiene 2 hijos
                sucesor = self.sucesor(deleted) #se crea sucesor como el nodo que devuelve el metodo sucesor
                print(f'***Se borro el nodo con dos hijos: {deleted} con un atributo.data = {deleted.data}, que sera sustituido por el nodo: {sucesor.data}')
                deleted.data = sucesor.data #El valor del nodo que se quiere eliminar pasara a ser el del nodo sucesor
                if sucesor.is_left == True: #Si el sucesor es un hijo izquierdo
                    if sucesor.left:
                        sucesor.papa.left = sucesor.left #Se reacomodan los apuntadores del padre e hijo del nodo a eliminar
                        sucesor.left.papa = sucesor.papa
                    else:
                        sucesor.papa.left = None #Su papa apuntara a None

                else: #Si no el sucesor es un hijo derecho
                    if sucesor.left: #Si el sucesor tiene un hijo a la izquierda
                        sucesor.papa.right = sucesor.left #Se reacomodan los apuntadores del padre e hijo del nodo a eliminar
                        sucesor.left.papa = sucesor.papa
                        sucesor.left.is_right = True #La banderas cambian
                        sucesor.left.is_left = False
                    elif sucesor.right: #o si tiene uno a la derecha
                        sucesor.papa.right = sucesor.right #Se reacomodan los apuntadores del padre e hijo del nodo a eliminar
                        sucesor.right.papa = sucesor.papa
                    else: #Si no, su papa apuntara a nada
                        sucesor.papa.right = None

                sucesor = None
            self.weight -= 1
                #Se eelimina el espacio de memoria de sucesor

    def sucesor(self, node): #Metodo para buscar la posicion mas a la derecha de la rama izquierda del nodo a eliminar
        itr = node.left #Se crea itr como la rama izquierda del nodo a eliminar
        itr_2 = itr.right #Se crea itr_2 como el hijo derecho de la rama izquierda
        if itr.right: #Si itr_2 no es Nule
            while itr_2.right: #Por el while se recorrera todo el arbol
                itr_2 = itr_2.right #Se actualiza itr_2
            itr = itr_2 #itr= pasara a ser la posicion encontrada
        return itr #Se devuelve itr

    def has_offspring(self, node): #Metodo para saber si un nodo tiene desendencia
        count = 0 #contador que iniciara en 0
        direction = None #variable para saber a donde apunta el hijo
        if node.right: #Si hay un nodo a la derecha
            count += 1 #la cuenta aumenta en uno
            direction = 'right' #direccion sera right
        if node.left: #si hay nodo a la izquierda
            count += 1 #contador aumenta en 1
            direction = 'left' #direction sera left
        return count, direction #se regresan ambas variables

    def height(self, node): #Metodo para conseguir la altura de un nodo

        # Verifica que no se haya mandado un nodo inexistente
        if node is None:
            # Si es verdad se regresa cero
            return 0
            #Recursivamente se busca la altura de los hijos izquierdos y derechos
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        #usando max se regresara la altura del hijo mas grande
        return max(left_height, right_height) + 1


    def get_bigger(self): #Metodo para conseguir el numero mas grande en el arbol
        if self.is_empty() == True: #Si no esta vacia acaba el metodo
            return

        itr = self.root #Se crea itr para ir recorriendo el arbol
        while True: #ciclo infinito
            if itr.right: #Mientras el arbol tenga hijo a la derecha
                itr = itr.right #si tiene hijo a la derecha, itr pasara a ser el hijo
            else:
                return itr #Cuando no tenga un hijo a la derecha se devolvera el nodo
    def get_smaller(self): #Metodo para conseguir el numero mas pequeno del arbol
        if self.is_empty() == True: #Si no esta vacia acaba el metodo
            return
        itr = self.root #Se crea itr para ir recorriendo el arbol
        while True: #ciclo infinito
            if itr.left:
                itr = itr.left #
            else:
                return itr #cuando no haya valor menor se devolvera el nodo

    def mirror(self, node): #MEtodo para invertir las posiciones de las subramas de un nodo
        if node == None: #Se verifica que el nodo enviado exista
            return #Si no existe se acaba el metodo
        else: #Si no
            aux_node = node #Se crea la variable auxiliar

            self.mirror(node.left) #Se llama recursivamente el metodo pero con los hijos izquierdos y derechos
            self.mirror(node.right)

            if node.left: #Si existe un hijo izquierdo
                node.left.is_left = False #Se cambian las banderas
                node.left.is_right = True
            if node.right: #Si existe un hijo derecho
                node.right.is_left = True #Se cambian las banderas
                node.right.is_right = False

            # Se intercambian las posiciones utilizando a aux_node para guardar el primer nodo que cambiara de posicion
            aux_node = node.left
            node.left = node.right
            node.right = aux_node

if __name__ == '__main__':

    print('#1 Recorrido PRE-ORDER manual: 67 44 22 9 37 39 50 47 85 73 90 88 94 ')
    Pino = Binary_tri()  # Se crea el arbol binario pino
    #datos = [67, 44, 85, 22, 50, 47, 9, 37, 39, 73, 90, 88, 94]  # Arreglo 'datos' con los valores que se agregaran al artbol pino
    datos = [67, 44, 22, 9, 37, 39, 50, 47, 85, 73, 90, 88, 94]  # Arreglo 'datos' con los valores que se agregaran al artbol pino
    # Ciclo for para agregar todos las posiciones del arreglo datos al arbol Pino
    for i in datos:
        Pino.add_node(i)  # Se agrega cada posicion del arreglo al arbol

    print('#2 Se Creo el siguiente arbol insertando los datos de acuerdo al PRE- ORDER: ')
    Pino.root.display() #Se imprime el arbol

    print('#3 ALTURA DEL ARBOL')
    Altura = Pino.height(Pino.root) #Se llama el metodo para conseguir la altura de la raiz del arbol
    print(f'La maxima altura del arbol es de: {Altura}\n')
    print('#4 VALOR MAYOR Y MENOR')
    Mayor = Pino.get_bigger() #Se llama el metodo para conseguir el numero mas grande del arbol
    Menor = Pino.get_smaller() #Se llama el metodo para conseguir el numero mas pequeo del arbol
    print(f'Mayor = {Mayor.data} -- Menor =  {Menor.data}\n')
    Pino.in_order(Pino.root) #Se llama el metodo in order
    print(' <-- #5 RECORRIDO "IN ORDER" \n')

    print('#6 NODOS BORRADOS')
    borrados = [73, 67, 50, 47, 39, 94] #Arreglo con los nodos que se van a eliminar
    for i in borrados: #Se recorre el arreglo borrado
        Pino.delete(i) #se va eliminando el nodo que toca del arreglo
        print('EL arbol quedara de la siguiente forma: ')
        Pino.root.display() #Se imprime como queda el arbol
        print('')

    print('#7 ARBOL ESPEJO\n')
    print('El ARbol queda de la siguiente forma: \n')
    Pino.mirror(Pino.root) #Se llama el metodo mirror que intercambiara las posiciones de los nodos
    Pino.root.display() #Se muestra como quedo el arbol
    print('')
    Pino.in_order(Pino.root) #Se ensena la representacion in order
    print(' <-- #7 RECORRIDO "IN ORDER" del arbol espejo \n')


    # ULTIMA MODIFICACION 28 DE OCTUBRE DEL 2021 A LAS 12 PM, TIJUANA BAJA CALIFORNIA