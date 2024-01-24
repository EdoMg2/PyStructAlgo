#PROYECTO ESTRUCTURA DE DATOS PARCIAL #2
#EQUIPO:
    #34226-LUIS VENTURA PARRA
    #33069-EDUARDO MENDOZA GOMEZ

def ask_for_integer(text_to_show): #Metodo para pedir un entero sacado de la clase de Programacion Orientada a Objetos
    while True:
        try:
            num = input(text_to_show)
            if num == '0' or num == ' 0' or num == '0 ' or num == ' 0 ':
                print('wtf')
                return 0
            num = int(num)
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

def list_checker(arr, search): #funcion para verificar a la hora de usar .index con un valor search en un arreglo arr
    try:
        A = arr.index(search) #Si existe el elemento en el arreglo se regresara la posicion
        return A
    except ValueError: #Si no se encuentra en la lista devolvera un None
        return None

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

   a = []
   for i in range(len(lista)):
       a.append(int(lista[i]))

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

class Node: #Clase Nodos que se utilizara en la clase arbol
#Se inicia la clase para los nodos
    def __init__(self, data, index, index_l, index_r):
        self.data = data #Se declara self.valor como el valor que sera enviado como parametro en cada instancia de la clase
        self.papa = None #Atributo para apuntar al padre de un nodo
        self.left = None #Atributo para apuntar a un hijo izquierdo de un nodo
        self.right = None #Atributo para apuntar a un hijo derecho de un nodo
        self.is_root = False #Atributo para saber si es raiz
        self.index = index #Atributo para saber la posiicion en la que fue introducido
        self.index_l = index_l #Atributo para saber las posiciones de los hijos izquierdos y derechos
        self.index_r = index_r

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

    # Metodos recuperados de: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

class Tree:
    def __init__(self,size):
        self.root = None #Se establece los valores iniciales de la raiz y peso del arbol
        self.weight = 0
        self.size = size #Atributo para que arbol no pase el numero de nodos que se le van a ingresar
        #Atributos necesarios para el proyecto
        self.nodes = [] #nodes guardara todos los nodos que sean agregados
        self.positions = [] #positions sera un arreglo con las posiciones del 0 a size-1
        for i in range(size):
            self.positions.append(i) #Se le agregan las posiciones
        self.iorder = [] #arreglo para guardar el orden del arbol cuando el metodo in order sea llamado
        self.children_positions = [] #Al igual que para positions, se creara un arreglo con todas las posiciones que los hijos pueden tener
        for i in range(size):
            self.children_positions.append(i) #Esta tendra desde 1 a size-1
        self.children_positions.pop(0) #Se le elimina el 0

    def is_empty(self): #Metodo que devolvera un True si la lista se encuentra vacia
        if self.weight == 0:
            return True

    def add_node(self, value, index, l, r): #Metodo para guardar los nodos
        if l > self.size - 1 or r > self.size - 1: #Se asegura que las posiciones de los hijos no sean mayores a la ultima posicion posible
            return False
        if l == r and l != -1: #Se asegura que no se repitan posiciones
            return False #Se regresan falso cuando no se guarda un nodo por un ingreso de datos erroneos

        self.positions.remove(index) #Se remueve la posicion del nodo agregado del arreglo con las posiciones
        check_children_l = list_checker(self.children_positions, l) #Se verifica que las posiciones de los hijos izquierdos e izquierdos esten dentro de las posibles
        check_children_r = list_checker(self.children_positions, r)
        node = Node(value, index, l, r) #se crea el nodo con los valores enviados como parametros


        if check_children_l != None and check_children_r != None: #Si ambas posiciones de los hijos son posibles
            self.add(node) #Se anade el nodo por el metodo add
            self.children_positions.remove(l) #se eliminan los indices de los hijos izquierods y derechos de la lista de indices de hijos
            self.children_positions.remove(r)
        elif check_children_l != None and r == -1: #Si se tiene un hijo izquierdo con una posicion posible, y el otro con -1
            self.add(node) #Se anade el nodo
            self.children_positions.remove(l) #Se remueve la posicion del hijo izquierdo
        elif check_children_r != None and l == -1: #De igual manera pero con el hijo derecho
            self.add(node)
            self.children_positions.remove(r)
        elif l == -1 and r == -1: #Si ambos indices de los hijos son igual a -1
            self.add(node) #Se anade el nodo y no se remueve ninguna posicion
        else:
            return False #Si los indices del nodo no encaja con ninguna de estas condiciones se devuelve un falso

        return True #Si se logra agregar un nodo correctamente se devuelve un True


    def add(self,node): #metodo para anadir nodos al arreglo de nodos
        if self.is_empty() == True: #Si el arbol esta vacio
            self.root = node #El nodo anadido sera la raiz del arbol
            node.is_root = True #Se cambia su bandera
        self.nodes.append(node) #Se agrega el nodo al arreglo
        self.weight += 1 #El peso del arbol aumenta en 1

    def give_children(self): #Metodo para armar el arbol
        for i in self.nodes: #Se recorre la lista de nodos
            if i.is_root == True: #el nodo raiz no tendra papa
                i.papa = None
            self.give_children_aux(i) #se llamara el metodo auxiliar enviando el nodo que se este recorriendo

    def give_children_aux(self, node): #metodo de apoyo para give_children
        if node.index_l == -1 and node.index_r == -1: #Si tiene ambos indices de hijos =- 1 ambos hijos seran None
            node.left = None
            node.right = None
        else: #Si tiene un indice diferente a -1
            left = self.give_children_browser(node.index_l) #Se buscara sus hijos izquierods y derechos por medio de give_children_browser
            right = self.give_children_browser(node.index_r) #enviando los indices de los hijos como parametros
            if left: #Si tiene hijo a la izquierda
                node.left = left #el hijo de nodo sera el que se encontr
                left.papa = node #El papa del encontrado sera el nodo
            if right: #De la misma manera con la subrama derecha
                node.right = right
                right.papa = node

    def give_children_browser(self, index): #Metodo para encontrar los hijos de un nodo, necesitara un index como parametro
        wanted_node = None #la variable wanted_node funcionara como el nodo a buscar
        for i in self.nodes: #se recorre la lista de nodos en el arbol
            if i.index == index: #Si el index del nodo del ciclo coincide con el buscado
                wanted_node = i #wanted_node pasara a ser el nodo
                return wanted_node #Se devolvera el nodo encontrado

        return wanted_node #si no se devolvera un None

    def in_order(self,node): #Metodo para mostrar los valores del arbol de acuerdo al orden in order
        # i - r - d
        if node: #Si se llama cuando el nodo no es None
            self.in_order(node.left) #Se llama el metodo de nuevo pero con el hijo izquierdo
            self.iorder.append(node.data) #Se le van agregando los datos al arreglo del atributo iorder
            self.in_order(node.right) #Se llama el metodo de nuevo pero con el hijo derecho

    def isnt_binary(self): #Metodo para saber si el arbol es binario por la representacion in_order
        self.in_order(self.root) #Se llama el metodo in_order
        error_flag = False #La bandera de error se encontrara en False en un inicio
        if len(self.iorder) == self.size: #Si la lista de in_order es del mismo tamano que el arbol
            for i in range(self.size): #se recorrera la lista
                if i != 0: #cuando i sea diferente a 0 para evitar comparar con una posicion menor a 0
                    if self.iorder[i-1] > self.iorder[i]: #Si el numero anterior es mayor al actual significara que el arbol no es binario
                        error_flag = True #Se devuelve la bandera en True
                        return error_flag
            return error_flag #Si no se devolvera en False

if __name__ == '__main__':
    Nodos = ask_for_integer('') #Se llama la funcion para conseguir un numero
    if Nodos == 0: #Si el vlaor que se envia es 0
        print('\nCORRECT') #El arbol sera correcto
    elif Nodos > 10 or Nodos < 0:
        print('\nINCORRECT')
    else: #Si no
        Arbol = Tree(Nodos) #Se crea el objeto Arbol dentro de la clase Tree con nodos como su tamano
        error_flag = False #Se crea la variable error_flag que servira para saber si hay errores
        for i in range(Nodos): #Ciclo for que se repetira el numero de nodos que se pidio
            entrada = lista_separada(' ') #Se pide los numeros de acuiuerdo a los parametros de input
            if entrada == False: #Si la funcion devuelve un falso
                error_flag = True #La bandera de error cambiara a True
            else: #Si no es asi se crearan las variables key, left, right como los primeros 3 valores devueltos por la funcion lista_separada
                key, left, right = entrada[0], entrada[1], entrada[2]
                check = Arbol.add_node(key,i, left, right) #check sera el dato booleano que devuelva el metodo add_node

        if check == True and error_flag == False: #Si check es True y la bandero de error nunca cambio a False
            Arbol.give_children() #Se llamara el metodo para crear el orden del arbol
            if Arbol.isnt_binary() == False: #Se llamara el metodo is not binary? y si esto devuelve una bandera de error False significara que lo es
                print('\nCORRECT\n') #Se imprime correct verificando que el arbol SI es binario
                Arbol.root.display() #Se llama display para mostrar el arbol desde la raiz
            else: #Si no es binario
                print('\nINCORRECT\n') #Se imprime INCORRECT
                Arbol.root.display() #Se muestra el arbol
        else: #Si hubo errores a la hora de crear el arbol o en el ingreso de las entradas, se imprimira INCORRECT
            print('\nINCORRECT')

# ULTIMA MODIFICACION 30 DE OCTUBRE DEL 2021 A LAS 2:00 PM, TIJUANA BAJA CALIFORNIA