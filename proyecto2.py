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
            node.papa = node_papa  # El padre del nuevo nodo sera la posicion devuelta
            self.weight += 1  # Al final del metodo, el arbol pesara uno mas
            if side == 'left': #Si el metodo devolvio un 'left' significara que el valor izquierdo de la posicion devuelta sera el nuevo nodo
                node_papa.left = node
                node.is_left = True #Se establece que el nodo creado es izquierda de otro
                return 0
            else: #Si no devolvio left significara que se encuentra a la derecha
                node_papa.right = node #el nuevo nodo sera un hijo derecho de la posicion deseada
                node.is_right = True #Se establece que es un hijo derecho
                return 1


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

                    deleted = None #SE elimina el espacio de memoria de deleted
            else: #Si el nodo tiene 2 hijos
                sucesor = self.sucesor(deleted) #se crea sucesor como el nodo que devuelve el metodo sucesor
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

class Pila:
    #Se crea el constructor con la variable tamano como variable
    def __init__(self, tamano):
        #Self. tamano sera usado para referenciar la cantidad de elementos en la lista
        self.tamano = tamano
        #Se muestra la lista iniciando en un arreglo vacio
        self.lista = []
        #Se inicia self.top para saber la ultima posicion del arreglo
        self.top = -1

    #Metodo para determinar si la lista esta vacia
    def esta_vacia(self):
        #En caso de que el top no haya avanzado la lista estara vacia
        if self.top == -1:
            return True
        #De lo contrrario no lo estara
        else:
            return False
    #Metodo para determinar si la lista esta llena
    def esta_llena(self):
        #En caso de que el top sea igual que la ultima posicion la lista estara llena
        if self.top == (self.tamano-1):
            return True
        #De lo contrrario no lo estara
        else:
            return False

    #Metodo para insertar un valor
    def inserar(self, item):
        if self.esta_llena() == False:
            #Se agrega e; valor deseado en la ultima posicion
            self.lista.append(item)
            #Top aumentara en 1 indicando la ultima posicion de la lista
            self.top += 1
        else:
            #print('La pila esta llena...')
            return False

    #Metodo para extraer un valor
    def extraer(self):
        #Si la lista esta vacia no se extrae ningun valor
        if self.esta_vacia() == True:
            #print('La pila esta vacia...')
            return False
        #Si contiene un valor se extrae el ultimo que fue agregado
        else:
            #Se saca el ultimo de la fila
            save = self.lista.pop(self.top)
            #Se guarda el valor extraido en caso de ser necesario
            self.top -=1
        #Se regresa el valor guardado
        return save

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

   if len(lista) != 3:
       return False

   a = Cola(10^5)
   for i in range(len(lista)):
       a.inserar(int(lista[i]))

   return a

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


if __name__ == '__main__':

    Numero_de_nodos = ask_for_integer('')
    Arbol = Binary_tri()
    error_flag = False
    order = []
    orderL = []
    orderR = []
    for i in range(Numero_de_nodos+1):
        entrada = lista_separada(' ')
        if entrada == False:
            error_flag = True
            break
        else:
            if Arbol.is_empty() == True:
                valor = entrada.extraer()
                Arbol.add_node(valor)
                #papa = Arbol.search(valor, Arbol.root)
                left = entrada.extraer()
                right = entrada.extraer()
                if Numero_de_nodos == 1:
                    error_flag = True
                    break
                elif left == -1 and right == -1:
                    error_flag = True
                    break
                else:
                    if left == -1:
                        if right != 1:
                            error_flag = True
                    elif right == -1:
                        if left != 1:
                            error_flag = True
                    else:
                        if left != 1 or right != 2:
                            error_flag = True

                        order.append(1)
                        order.append(2)
            else:
                valor = entrada.extraer()
                lado = Arbol.add_node(valor)

                if left == -1:
                    if lado == 0 or right != order[len(order)-1]+1:
                        error_flag = True
                        order = order + order[len(order) - 1] + 1
                elif right == -1:
                    if lado == 1 or left != order[len(order)-1]+1:
                        error_flag = True
                        order = order + order[len(order)-1]+1

                papa = Arbol.search(valor, Arbol.root)
                left = entrada.extraer()
                right = entrada.extraer()

    if error_flag == True:
        print('INCORRECT')

    else:
        print('CORRECT')
    print(Arbol.root.data, Arbol.root.left.data, Arbol.root.right.data)
    Arbol.root.display()
    print('order: ',order)








