#Meta 2.4 AVL-completo
#Hacer un programa que cumpla con las instrucciones de la Meta 2.4
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
        self.height = 1 #Atributo para saber la altura de cada nodo

    def getData(self): #Metodo para llamar al valor del nodo
        return self.data


    def display(self): #Metodo para visualizar la descendencia de un nodo
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self): #Metodo auxiliar de display
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

        #Metodos recuperados de: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

class Bb_tree: #Clase para arboles avl
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
            node.papa = node_papa #El padre del nuevo nodo sera la posicion devuelta

            if side == 'left': #Si el metodo devolvio un 'left' significara que el valor izquierdo de la posicion devuelta sera el nuevo nodo
                node_papa.left = node
                node.is_left = True #Se establece que el nodo creado es izquierda de otro
                self.inspect_insertion(node)

            else: #Si no devolvio left significara que se encuentra a la derecha
                node_papa.right = node #el nuevo nodo sera un hijo derecho de la posicion deseada
                node.is_right = True #Se establece que es un hijo derecho
                self.inspect_insertion(node)

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
                #deleted = None #el espeacio de memoria se elimina

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

            else: #Si el nodo tiene 2 hijos
                sucesor = self.sucesor(deleted) #se crea sucesor como el nodo que devuelve el metodo sucesor
                deleted.data = sucesor.data #El valor del nodo que se quiere eliminar pasara a ser el del nodo sucesor
                if sucesor.data <= sucesor.papa.data: #Si el sucesor es un hijo izquierdo
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
            self.inspect_deletion(deleted) #Se llama el metodo inspect_deletion  para inspeccionar que el nodo eliminado no haya desbalanceado al arbol
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

    def right_rotate(self,z): #Metodo para hacer la rotacion hacia la derecha
        sub_root = z.papa #Sub_root sera el papa del nodo pasado como z
        y = z.left #y sera el hijo a la izquierda de z
        t3 = y.right #t3 su hijo a la derecha
        #Se reacomodan los nuevos hijos y padres de y y z
        y.right = z
        z.papa = y
        z.left = t3
        z.is_right = True
        z.is_left = False
        if t3 != None: #Si existe un t3
            t3.papa = z #t3 pasara a ser el padre de z
            t3.is_left = True
            t3.is_right = False

        y.papa = sub_root #el nuevo papa de y sera el antiguo de z

        if y.papa ==None: #Si el papa de y es ninguno
            self.root = y #Significara que y sera la raiz y se cambia la bandera
            y.is_root = True
        else: #Si tiene papa, se cambiaran los apuntadores de su padre
            if y.papa.left == z: #si su apuntador izquierdo es z, se le asignara ahora a y
                y.papa.left = y
                y.is_left = True
                y.is_right = False

            else: #Si no el apuntador de la derecha apuntara a y
                y.papa.right = y
                y.is_right = True
                y.is_left = False

        # Se reasignan las nuevas alturas de z y y
        z.height = 1+max(self.get_height(z.left),self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def left_rotate(self,z): #Metodo para las rotaciones hacia la izquierda
        sub_root = z.papa #la subruta sera el papa de z
        y = z.right #la derecha de z sera y
        t2 = y.left #t2 sera el hijo izquierdo de y
        y.left = z #se reasignan las nuevas posiciones de acuerdo a la rotacion
        z.papa = y
        z.is_left = True #Se cambian las banderas de z
        z.right = False
        z.right = t2 #t2 sera el hijo derecho de z
        if t2 != None: #Si hay t2
            t2.papa = z #Su papa sera z
            t2.is_right = True #Se reasignan sus nuevas banderas
            t2.is_left = False

        y.papa = sub_root  # el nuevo papa de y sera el antiguo de z

        if y.papa == None: #Si y no tiene papa significara que sera la nueva raiz del arbol
            self.root = y #se reasigna como nueva raiz y sus banderas cambian
            y.is_root = True
            y.is_left = False
            y.is_right = False
        else: #Si no
            if y.papa.left == z: #Si el hijo izquierdo de su papa es z, pasara a ser y
                y.papa.left = y
                y.is_left = True #Se cambian las banderas
                y.is_right = False
            else:
                y.papa.right = y #y sera un hijo izquierdo de su padre
                y.is_right = True #Se cambian las banderas
                y.is_left = False

        # Se reasignan las nuevas alturas de z y y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, cur_nodo): #Metodo para conseguri la altura de un nodo
        if cur_nodo == None: #si el nodo enviado no existe
            return 0 #se regresa 0
        return cur_nodo.height #si no se enviara su altura

    def taller_child(self,cur_nodo): #Metodo para saber que hijo tiene mas altura
        left = self.get_height(cur_nodo.left) #la izquierda sera la altura de los nodos a la izquierda
        right = self.get_height(cur_nodo.right) #la derecha sera la altura de los nodo a la derecha
        if left >= right:  #Si la izquierda es mayor a la derecha
            return cur_nodo.left #se regresa el nodo izquierdo
        else:
            return cur_nodo.right #si no se regresa el derecho

    def inspect_insertion(self,cur_nodo, path=[]): #Metodo que inspeccionara el balanceo del arbol al insertar un elemento
        if cur_nodo.papa == None: return
        path = [cur_nodo] + path
        left_height = self.get_height(cur_nodo.papa.left)
        right_height = self.get_height(cur_nodo.papa.right)
        #print('altura,izq y der:',left_height,right_height)

        if abs(left_height-right_height) > 1: #Si la diferencia entre la altura de las ramas izquierdas y derechas es mayor a 1
            path = [cur_nodo.papa] + path #El path agregara al papa del nodo actual
            self.rebalance_nodo(path[0], path[1], path[2]) #Se rebalanceara el nodo con los primeros tres elementos de path como parametro
            return #Se acabara el metodo
        new_height = 1 + cur_nodo.height
        if new_height > cur_nodo.height:
            cur_nodo.papa.height = new_height

        self.inspect_insertion(cur_nodo.papa, path) #Se llama el metodo inspect_insertion para balancear el nodo

    def rebalance_nodo(self, z, y, x): #Metodo para volver a balancear el arbol
        if y == z.left and x == y.left: #Si y es igual a la izquierda de z y x igual a la izquierda de y
            self.right_rotate(z) #Se hara una rotacion hacia la derecha
        elif y == z.left and x == y.right: #Si y es igual a la izqeuirda de z y x es igual a la derecha de y
            self.left_rotate(y) #se hace una rotacion a la izquierda a partir de y y luego una a la derecha a partir de z
            self.right_rotate(z)
        elif y == z.right and x == y.right: #si y es igual a la derecha de z y x a la derecha de y
            self.left_rotate(z) #se hace una rotacion hacia la izquierda a parter de z
        elif y == z.right and x == y.left: #si y es igual a la derecha de z y x es igual a la izquierda de y
            self.right_rotate(y) #se hace una rotacion a la derecha a partir de y y despues una a la izquierda a partir de z
            self.left_rotate(z)
        else: #si no
            raise Exception('z,y,x configuracion del nodo no reconocida') #excepcion para cuando no se envia una configuracion adecuada

    def inspect_deletion(self,cur_nodo): #Metodo para inspeccionar cada vez que se elimine un nodo

        if cur_nodo == None: return #si no hay nodo actual se acabara el metodo
        # las alturas derecha e izquierda seran los numeros regresados por el metodo get_height con los subramas izquierda y derecha
        left_height = self.get_height(cur_nodo.left)
        right_height = self.get_height(cur_nodo.right)
        if abs(left_height-right_height)> 1: #Si la diferencia entre las dos alturas es mayor a 1
            y = self.taller_child(cur_nodo) #Se crea y llamando al metodo taller_child con el nodo actual como parametro
            x = self.taller_child(y) #Se llama el metodo taller_child con y como parametro
            self.rebalance_nodo(cur_nodo, y, x) #se llama el metodo de rebalance_nodo con el nodo actual, y y x como parametros
        self.inspect_deletion(cur_nodo.papa) #Se llama a si mismo de manera recursiva con el padre de su hijo

if __name__ == '__main__':
    Pino = Bb_tree() #Se crea la instancia Pino como el arbol que se usara de ejemplo
    print('***** Meta 2.4 AVL-completoMeta 2.4 AVL-completo *****\n')
    print('Se ha creado el arbol Pino: ')
    datos = [7, 8, 6, 9, 22, 18, 21, 20, 43, 44, 45, 10, 16]
    for i in datos: #Por medio de un for se ira agregando y mostrando cada numero dentro de datos al arbol
        Pino.add_node(i)
        print(f'\nSe ha agregado el numero {i} de tal forma que el arbol queda de la siguiente forma: ')
        Pino.root.display() #Se llama el metodo de la raiz para mostrar a su desendencia

    print('***ELIMINACIONES***')
    datos_2 = [8, 20, 43, 22, 45]
    for i in datos_2: #Por medio de un for se ira agregando y mostrando cada numero dentro de datos al arbol
        Pino.delete(i)
        print(f'\nSe ha eliminado el numero {i} de tal forma que el arbol queda de la siguiente forma: ')
        Pino.root.display()  # Se llama el metodo de la raiz para mostrar a su desendencia

    busqueda = Pino.search(9, Pino.root)
    print('x')
    print(busqueda.height)


# ULTIMA MODIFICACION 22 DE OCTUBRE DEL 2021 A LAS 2:00 PM, TIJUANA BAJA CALIFORNIA