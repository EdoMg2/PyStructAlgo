# META 3.1 ARBOL B PARTE-1
# Sube tu programa con la función de insertar y de buscar para arboles B
# 33069-EDUARDO MENDOZA GOMEZ

class Node:  # Clase para los nodos del arbol B
    def __init__(self, t):  # t = numero minimo de hijos de cada nodo
        self.hoja = 1  # El valor de los numeros de hijos
        self.hijos = []  # Arreglo que tendra los hijos de un nodo
        self.keys = []  # Arreglo que tendra los valores dentro de un nodo
        self.n = 0  # N de llaves en el nodo
        for i in range(2 * t + 1):  # Se agregan todos los espacios que hay dentro de un nodo
            self.keys.append([None])

        for i in range(2 * t + 1):  # De igual manera con los hijos
            self.hijos.append([None])


class Arbol_B:  # Clase de arboles B
    def __init__(self,
                 gradoMimo):  # Constructor del arbolB en donde gradoMInimo sera el numero minimo de keys en un hijo y sera enviado como parametro
        self.t = gradoMimo
        self.root = None

    def bTreeCreate(self):  # Metodo para crear un nuevo arbol b
        if self.root == None:
            self.root = Node(self.t)
        return self.root

    def bTreeSplit(self, x, i):
        z = Node(self.t)  # Se crea un nuevo nodo pasandole t
        y = x.hijos[i]  # copia en y el hijo en la posicion i
        z.hoja = y.hoja  # copia los datos de la hoja y en la nueva hoja
        z.n = self.t  # Actualiza el valor de n con t
        for j in range(1, self.t + 1):  # for que acabara hasta el numero minimo de keys
            # print(f'VALOR {y.keys[j+self.t]} Y POSICION EN LLAVES {j+self.t}') #se imprimen
            z.keys[j - 1] = y.keys[j + self.t]  # copia las llaves al nuevo nodo
            y.keys[j + self.t] = None  # borra las llaves del viejo nodo
            y.n -= 1
        if y.hoja == 0:
            for j in range(0, self.t + 1):
                # print('posiciones de los hijos', y.hijos[j+self.t], j+self.t)
                z.hijos[j] = y.hijos[j + self.t]  # Copia los hijos al nuevo nodo
                y.hijos[j + self.t] = None  # Se actualiza en None
            y.n = self.t  # Actualiza el valor de n del nodo

        for j in range(x.n, i - 1, -1):  # Valores que se quedan en el nodo
            x.hijos[j + 1] = x.hijos[j]
            # print('entra a  recorrer hijos', x.hijos[j+1])
        x.hijos[i + 1] = z  # Se actualiza el hijo en la posicion i+1
        # print(f'x.hijos[0]-->{x.hijos[0].keys}, x.hijos[1]-->{x.hijos[1].keys}')

        for j in range(x.n, i - 1, -1):
            # print(f'2nd for: x.n= {x.n}, i-1: {i-1}')
            x.keys[j + 1] = x.keys[j]
            # print('entra a recorrer llaves', x.keys[j+1])
        x.keys[i] = y.keys[self.t]  # Se agrega un nuevo valor en el nodo papa
        y.keys[self.t] = None  # El valor asignado al papa se eliminara del hijo
        y.n -= 1  # El numero de keys disminuye
        # print(f'x.keys --> {x.keys}, x.hijos[0]-->{x.hijos[0].keys}, x.hijos[1]-->{x.hijos[1].keys}')
        x.n = x.n + 1

    def bTreeInsertNonFull(self, x, k):
        i = x.n  # i sera el numero de keys en el nodo
        if x.hoja == 1:  # Si el nodo es hoja
            while (i >= 1) and k < x.keys[
                i - 1]:  # si i es 1 o superior y al mismo tiempo la  posicion anterior en x.keys es mayor a k
                x.keys[i] = x.keys[i - 1]  # keys[i] sera la misma que el anterior
                i = i - 1  # i disminuira en uno
            if i == 0:  # Si i llega a 0
                x.keys[i] = k  # keys[i] sera k
            else:  # Si no adaptara su valor de i
                x.keys[i] = k
            x.n = x.n + 1  # El numero de keys aumentara en uno

        else:  # No es hoja
            while (i >= 1) and (k < x.keys[i - 1]):  # de igual manera un ciclo while para encontrar la posicion en la lista de keys
                i = i - 1  # i retrocera cada vez que se cumpla la condicion del while
            # i = i+1
            #print('#i = ',i)
            # leer a disco
            # print(f'x.hijos[i].n= {x.hijos[i].n}')
            if x.hijos[i].n == 2 * self.t:  # Si el hijo en la posicion i del nodo esta lleno
                #print('ERROR: ',x.keys, i,x.keys[i])
                if self.t != 1:
                    if k > x.keys[i]:
                        i = i + 1
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva
                self.bTreeSplit(x, i)
            else:
                # print(f'aw here we go again: i= {i} --> {x.hijos[i].keys}, K:D --> {k} n--> {x.hijos[i].n}')
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva

    def bTreeInsert(self, node, k):  # Metodo que sera llamado cada vez que se agregue un nodo
        r = self.root  # r sera la raiz del arbol
        # nodo lleno
        if r.n == 2 * self.t:  # Si la raiz se encuentra llena
            s = Node(self.t)  # El nuevo nodo s sera la nueva raiz
            self.root = s
            s.hoja = 0  # Se establece que no sera un nodo hoja y que no cuenta con keys dentro
            s.n = 0
            s.hijos[0] = r  # Su hijo sera la antigua raiz
            self.bTreeInsertNonFull(r, k)  # Se llama el metodo para insertar el nuevo valor
            # print(r.keys, 'A')
            # print(f'Index: {s.hijos.index(r)}')
            # self.bTreeSplit(s, 0)
            self.bTreeSplit(s, s.hijos.index(r))
            # self.bTreeInsertNonFull(s, k)
        else:
            self.bTreeInsertNonFull(r, k)

    def bTreeSearch(self, nodo, k):
        x = nodo  # x sera el nodo enviado como parametro
        i = 0  # i empezara en una constante
        while i < x.n and k > x.keys[i]:  # Ciclo while para explorar nodos
            i += 1  # i aumentara en uno
        # print(f'i = {i}, llaves del nodo = {x.keys[i]}') #Mensaje que indica la posicion en la que se esta buscando
        if i <= x.n and k == x.keys[i]:  # Si el ciclo while se ucmple
            return (x, i)  # Se regresa el nodo encontrado y la posicion
        else:
            if x.hoja == 1:
                return None, None  # No existe, y se regresa un None
            else:  #
                return self.bTreeSearch(x.hijos[i],k)  # Se llama el metodo de manera recursiva con el nodo hijo en la posicion i

    def delete_value(self, k):
        (node, position_in_node) = PinoB.bTreeSearch(self.root, k)

        if node.hoja == 1:
            if node.n > self.t:
                if node.keys[position_in_node+1] == [None]:
                    node.keys[position_in_node] = [None]
                else:
                    i = position_in_node
                    node.keys[position_in_node] = [None]
                    for j in range(i+1):
                        if node.keys[j] == [None]:
                            for l in range(j, node.n-1):
                                node.keys[l] = node.keys[l+1]
                            node.keys[l+1] = [None]

    def print_tree(self, x, l=0):
        print("Level ", l, " ", end=":")
        for i in x.children:
            print(i, end=" ")
        print()
        l += 1
        if len(x.hijos) > 0:
            for i in x.hijos:
                self.print_tree(i, l)



if __name__ == '__main__':

    PinoB = Arbol_B(2)  # se crea el arbol B con 2 como el numero minimo de llaves por en cada hijo
    actual = PinoB.bTreeCreate()  # Actual sera la raiz del arbol
    print('*** INSERCION A LA RAIZ ***\n')
    print('Nodo Creado: ', PinoB.root.keys)

    data = [96, 111, 85, 16]  # array con valores quese agregaran al arbol
    j = 1  # variable que servira como contador
    for i in data:  # Ciclo for para ir agregando los datos
        PinoB.bTreeInsert(actual, i)  # Se agrega el dato junto a la impresion de un mensaje
        print(f'#{j}: {PinoB.root.keys}')
        j += 1  # j aumenta en 1

    # Se agrega un valor que hara cambiar la raiz del arbol por lo que se imprime aparte
    print('\n*** INSERCIONES QUE GENERARAN NODOS HIJOS ***\n')
    PinoB.bTreeInsert(actual, 80)
    print(f'ROOT-- n: {PinoB.root.n}, keys: {PinoB.root.keys}, leaf: {PinoB.root.hoja}, HIJOS- [0]: {PinoB.root.hijos[0].keys}, [1]: {PinoB.root.hijos[1].keys}')

    # Se vuelven a agregar nuevos valores al array data y de la misma forma se agregararan al arbol
    data = [81, 82, 100, 83, 84, 112]
    j = 1
    actual = PinoB.bTreeCreate()

    for i in data:  # En el ciclo for se le iran agregando los valores de data junto a un mensaje
        PinoB.bTreeInsert(actual, i)
        if i != 83 and i != 84 and i != 112:  # Cuando se agregan valores distintos al ultimo se mostraran la raiz y sus dos hijos
            print(
                f'#{j}: ROOT--> n: {PinoB.root.n}, keys: {PinoB.root.keys}, leaf: {PinoB.root.hoja}, HIJOS--> [0]: {PinoB.root.hijos[0].keys}, [1]: {PinoB.root.hijos[1].keys} ')
        else:  # Pero cuando llegue al ultimo valor (83) un nodo hijo estara lleno por lo que se tendra que subir un valor a la raiz y por ello agregar un nuevo nodo hijo
            print(
                f'#{j}: ROOT--> n: {PinoB.root.n}, keys: {PinoB.root.keys}, leaf: {PinoB.root.hoja}, HIJOS--> [0]: {PinoB.root.hijos[0].keys}, [1]: {PinoB.root.hijos[1].keys}, [2]: {PinoB.root.hijos[2].keys}')
        j += 1

    print('\n*** BUSQUEDAS ***\n')  # Busqueda un valor en cada uno de los nodos del arbol imprimiendo los valores que regresa el metodo de busqueda

    (nodo, posicion) = PinoB.bTreeSearch(PinoB.root, 85)
    print(f'Encontrado el valor 85 en el nodo: {nodo.keys} en la posicion {posicion}')

    (nodo, posicion) = PinoB.bTreeSearch(PinoB.root, 16)
    print(f'Encontrado el valor 16 en el nodo: {nodo.keys} en la posicion {posicion}')

    (nodo2, posicion) = PinoB.bTreeSearch(PinoB.root, 84)
    print(f'Encontrado el valor 84 en el nodo: {nodo2.keys} en la posicion {posicion}')

    (nodo, posicion) = PinoB.bTreeSearch(PinoB.root, 111)
    print(f'Encontrado el valor 111 en el nodo: {nodo.keys} en la posicion {posicion}')

    PinoB.delete_value(96)
    print(nodo.keys)


    #PinoB.print_tree(PinoB.root)
    """PinoB = Arbol_B(1)
    actual = PinoB.bTreeCreate()
    print('*** INSERCION A LA RAIZ ***\n')
    print('Nodo Creado: ', PinoB.root.keys)

    data = [96, 111, 85, 16, 112, 100, 101]
    j = 1
    for i in data:
        PinoB.bTreeInsert(actual, i)
        print(f'#{j}: {PinoB.root.keys}')
        j += 1
    print(PinoB.root.keys, PinoB.root.hijos[0].keys, PinoB.root.hijos[1].keys, PinoB.root.hijos[0].hijos[0].keys)"""