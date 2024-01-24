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

    def show(self, counter=0):
        """Prints the keys at each level."""
        if counter == 0:
            print()

        print(counter, str(self.keys), self.n)

        # Recursively print the key of child nodes (if these exist).
        if self.hoja == 0:
            for item in self.hijos:
                try:
                    item.show(counter + 1)
                except:
                    AttributeError


class Arbol_B:  # Clase de arboles B
    def __init__(self,
                 gradoMimo):  # Constructor del arbolB en donde gradoMInimo sera el numero minimo de keys en un hijo y sera enviado como parametro
        self.t = gradoMimo
        self.root = [None]

    def bTreeCreate(self):  # Metodo para crear un nuevo arbol b
        if self.root == [None]:
            self.root = Node(self.t)
        return self.root

    def bTreeSplit(self, x, i, excepcion_flag=False):

        z = Node(self.t)  # Se crea un nuevo nodo pasandole t
        y = x.hijos[i]  # copia en y el hijo en la posicion i
        # print(x.keys, 'y =', y.keys)
        # y.show()
        z.hoja = y.hoja  # copia los datos de la hoja y en la nueva hoja
        z.n = self.t  # Actualiza el valor de n con t
        for j in range(1, self.t + 1):  # for que acabara hasta el numero minimo de keys
            # print(f'VALOR {y.keys[j+self.t]} Y POSICION EN LLAVES {j+self.t}') #se imprimen
            z.keys[j - 1] = y.keys[j + self.t]  # copia las llaves al nuevo nodo
            y.keys[j + self.t] = [None]  # borra las llaves del viejo nodo
            y.n -= 1
        # print(f'z: {z.keys} , y = {y.keys}')
        if y.hoja == 0:
            for j in range(1, self.t + 2):
                # print(f'j:{j}, y= {y.hijos[2].keys}')
                z.hijos[j - 1] = y.hijos[j + self.t]  # Copia los hijos al nuevo nodo
                y.hijos[j + self.t] = [None]  # Se actualiza en None
            y.n = self.t + 1  # Actualiza el valor de n del nodo

            # print(f'hijos de y{y.hijos}, {y.hijos[0].keys} {y.hijos[1].keys}, hijos de z{z.hijos[0].keys}')
        if x.n == 2 * self.t:
            x.hijos.insert(i + 1, z)

            key = y.keys[y.n - 1]
            y.keys[y.n - 1] = [None]
            y.n -= 1
            for o in range(x.n):
                if x.keys[o]:
                    if key < x.keys[o]:
                        break
            x.keys.insert(o + 1, key)
            x.keys.pop()
            x.n += 1
            # print(x.keys, x.n, y.keys,y.n, z.keys, z.n)
            s = Node(self.t)  # El nuevo nodo s sera la nueva raiz
            self.root = s
            s.hoja = 0  # Se establece que no sera un nodo hoja y que no cuenta con keys dentro
            s.n = 0
            s.hijos[0] = x  # Su hijo sera la antigua raiz
            self.bTreeSplit(s, s.hijos.index(x), True)
            # x.hijos.pop()



        else:

            for j in range(x.n, i - 1, -1):  # Valores que se quedan en el nodo
                x.hijos[j + 1] = x.hijos[j]

            x.hijos[i + 1] = z  # Se actualiza el hijo en la posicion i+1
            # print(f'x.hijos[0]-->{x.hijos[0].keys}, x.hijos[1]-->{x.hijos[1].keys}')
            # print(f'PRE-end: y:{y.keys}, z:{z.keys}, x = {x.keys}')

            for j in range(x.n, i - 1, -1):
                x.keys[j + 1] = x.keys[j]
                # print('entra a recorrer llaves', x.keys[j+1])
            x.keys[i] = y.keys[self.t]  # Se agrega un nuevo valor en el nodo papa
            y.keys[self.t] = [None]  # El valor asignado al papa se eliminara del hijo
            y.n -= 1  # El numero de keys disminuye
            # print(f'x.keys --> {x.keys}, x.hijos[0]-->{x.hijos[0].keys}, x.hijos[1]-->{x.hijos[1].keys}')
            x.n = x.n + 1
            # print(f'end: y:{y.keys}, z:{z.keys}, x = {x.keys}')

    def bTreeInsertNonFull(self, x, k, clave=False):
        i = x.n  # i sera el numero de keys en el nodo
        if x.hoja == 1 or clave == True:  # Si el nodo es hoja
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
            while (i >= 1) and (
                    k < x.keys[i - 1]):  # de igual manera un ciclo while para encontrar la posicion en la lista de keys
                i = i - 1  # i retrocera cada vez que se cumpla la condicion del while
            # i = i+1

            # print('#i = ',i)
            # leer a disco
            if x.hijos[i] == [None]:
                x.hijos[i] = Node(self.t)

            if x.hijos[i].n == 2 * self.t:  # Si el hijo en la posicion i del nodo esta lleno
                # print('ERROR: ',x.keys, i,x.keys[i])

                '''if self.t != 1:
                    if k == 120:
                        print(f'Se comparara k: {k} con x.keys{x.keys} en la posicion i:  {i}')
                    if k > x.keys[i]:
                        i = i + 1'''
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva

                # print(f'Se enviara k = {k}, e i= {i}')
                self.bTreeSplit(x, i)
            else:
                # print('chill')
                # print(f'aw here we go again: i= {i} --> {x.hijos[i].keys}, K:D --> {k} n--> {x.hijos[i].n}')
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva

    def bTreeInsert(self, k):  # Metodo que sera llamado cada vez que se agregue un nodo
        r = self.root  # r sera la raiz del arbol
        # nodo lleno
        # print(f'numero:{k}, r.n:{r.n}')
        if r.n == 2 * self.t and self.check_children(r) == True:  # Si la raiz se encuentra llena
            # print(k,'?')
            s = Node(self.t)  # El nuevo nodo s sera la nueva raiz
            self.root = s
            s.hoja = 0  # Se establece que no sera un nodo hoja y que no cuenta con keys dentro
            s.n = 0
            s.hijos[0] = r  # Su hijo sera la antigua raiz
            self.bTreeInsertNonFull(r, k, True)  # Se llama el metodo para insertar el nuevo valor
            # print(r.keys, 'A')
            # print(f'Index: {s.hijos.index(r)}')
            # self.bTreeSplit(s, 0)
            self.bTreeSplit(s, s.hijos.index(r))
            # self.bTreeInsertNonFull(s, k)
        else:
            self.bTreeInsertNonFull(r, k)

    def bTreeSearch(self, nodo, k, papa=None, positionaschild=None):
        x = nodo  # x sera el nodo enviado como parametro
        i = 0  # i empezara en una constante
        while i < x.n and k > x.keys[i]:  # Ciclo while para explorar nodos
            i += 1  # i aumentara en uno
        # print(f'i = {i}, llaves del nodo = {x.keys[i]}') #Mensaje que indica la posicion en la que se esta buscando
        if i <= x.n and k == x.keys[i]:  # Si el ciclo while se ucmple
            return (x, i, papa, positionaschild)  # Se regresa el nodo encontrado y la posicion
        else:
            if x.hoja == 1:
                return [None], [None], [None], [None]  # No existe, y se regresa un None
            else:  #
                return self.bTreeSearch(x.hijos[i], k, x,
                                        i)  # Se llama el metodo de manera recursiva con el nodo hijo en la posicion ix

    def delete_value(self, k):
        (node, position_in_node, papa, position_as_child) = self.bTreeSearch(self.root, k)
        if node == [None]:
            print('Clave no presente en el arbol...')
        else:
            if node.hoja == 1:
                if node.n > self.t:
                    if node.keys[position_in_node + 1] == [None]:
                        node.keys[position_in_node] = [None]
                    else:
                        self.shift_node(node, position_in_node)

                    node.n -= 1

                else:
                    if position_in_node == node.n - 1:
                        node.keys[position_in_node] = [None]

                    else:
                        self.shift_node(node, position_in_node)

                    self.get_sucesor(node, position_in_node, papa, position_as_child)

            else: #No es hoja
                (node_sucesor, sucesor, position_sucesor, sflag) = self.get_sucesor(node, position_in_node)
                (s_node_s, s_position_in_node, s_papa, s_position_as_child) = self.bTreeSearch(self.root, sucesor)
                print(sucesor)
                node.keys[position_in_node] = sucesor
                self.shift_node(node_sucesor, position_sucesor)
                node_sucesor.n -= 1
                error_f = self.check_keys(node_sucesor)
                print(error_f)




    def shift_node(self, node, position_in_node):
        i = position_in_node  # Forma de desplazar
        save = node.keys[i]
        node.keys[i] = [None]

        for j in range(i + 1):
            if node.keys[j] == [None]:
                for l in range(j, node.n - 1):
                    node.keys[l] = node.keys[l + 1]
                node.keys[l + 1] = [None]
        return save

    def check_children(self, node):

        if len(node.hijos) == 2 * self.t + 1:
            for i in node.hijos:
                if i == [None] or None:
                    return True
                # print(f'se imprime {i.keys}')
                for j in range(2 * self.t):
                    if i.keys[j] == [None]:
                        # print(f'En el nodo {i.keys} la clave {i.keys[j]}, en la posicion {j}')
                        return False
            return True
        else:
            return False

    def get_sucesor(self, node, position_in_node, papa=None, position_as_child=None):

        if node.hoja == 1:  # Si es hoja

            if papa.hijos[position_as_child + 1] != [None]:
                if papa.hijos[position_as_child + 1].n > self.t:
                    node.keys[node.n - 1] = papa.keys[position_as_child]
                    papa.keys[position_as_child] = papa.hijos[position_as_child + 1].keys[0]
                    self.shift_node(papa.hijos[position_as_child + 1], 0)
                    papa.hijos[position_as_child + 1].n -= 1

                elif papa.hijos[position_as_child - 1] != [None]:
                    if papa.hijos[position_as_child - 1].n > self.t:
                        node.keys.insert(0, papa.keys[position_as_child - 1])
                        node.keys.pop()
                        papa.hijos[position_as_child - 1].keys[papa.hijos[position_as_child - 1].n - 1] = [None]
                        papa.hijos[position_as_child - 1].n -= 1

                elif papa.hijos[position_as_child + 1] != [None]:
                    node.keys[node.n - 1] = papa.keys[position_as_child]
                    self.merge_nodes(node, papa, papa.hijos[position_as_child + 1], 'right')

                    for long in range(position_as_child + 1, len(papa.hijos) - 1):
                        papa.hijos[long] = papa.hijos[long + 1]
                    (X, XX, grandpa, p_position_as_child) = self.bTreeSearch(self.root, papa.keys[0])
                    self.shift_node(papa, position_as_child)
                    self.ask_for_key(papa, position_as_child, grandpa)


                else:
                    print('xD2')
                    (X, XX, grandpa, p_position_as_child) = self.bTreeSearch(self.root, papa.keys[0])
                    node.keys.insert(0, papa.keys[position_as_child - 1])
                    node.keys.pop()
                    self.ask_for_key(node, position_as_child, papa)
                    papa.keys[papa.n - 1] = [None]
                    self.ask_for_key(papa, p_position_as_child, grandpa)


            elif papa.hijos[position_as_child - 1] != [None]:
                if papa.hijos[position_as_child - 1].n > self.t:
                    node.keys.insert(0, papa.keys[position_as_child - 1])
                    node.keys.pop()
                    papa.hijos[position_as_child - 1].keys[papa.hijos[position_as_child - 1].n - 1] = [None]
                    papa.hijos[position_as_child - 1].n -= 1

                else:
                    print('xD2')
                    (X, XX, grandpa, p_position_as_child) = self.bTreeSearch(self.root, papa.keys[0])
                    node.keys.insert(0, papa.keys[position_as_child-1])
                    node.keys.pop()
                    self.ask_for_key(node, position_as_child, papa)
                    papa.keys[papa.n-1] = [None]
                    self.ask_for_key(papa, p_position_as_child, grandpa)



        else:  # Si no es hoja
            itr = node.hijos[position_in_node]
            if itr == [None]:  # Izquierda
                while itr != [None]:
                    itr_re = itr
                    itr = itr.hijos[0]

                sucesor = itr_re.keys[itr_re.n - 1]
                sideflag = 'left'
                return itr_re, sucesor, itr_re.n - 1, sideflag
            else:  # Derecha
                itr = node.hijos[position_in_node + 1]
                while itr != [None]:
                    count = 0
                    for i in itr.hijos:
                        # print(f'#0ITR: {itr.keys}')
                        if i == [None]:
                            itr_re = itr
                            itr = itr.hijos[count]
                            # print(f'#1ITR: {itr}, PREITR: {itr_re.keys}')

                            break
                        count += 1

                sucesor = itr_re.keys[0]
                sideflag = 'right'
                return itr_re, sucesor, 0, sideflag


    def ask_for_key(self, node, position_as_child, papa):
        if papa.hijos[position_as_child+1] != [None]:       #Si tiene un nodo hermano derecho

            if papa.hijos[position_as_child+1].n > self.t:
                key = self.shift_node(papa.hijos[position_as_child+1], 0)
                papa.hijos[position_as_child + 1].n -= 1
                if papa.hijos[position_as_child+1].hoja == 0:
                    save = papa.hijos[position_as_child+1].hijos[0]

                    for i in range(0, len(papa.hijos[position_as_child+1].hijos)-1):
                        papa.hijos[position_as_child + 1].hijos[i] = papa.hijos[position_as_child+1].hijos[i+1]
                    node.hijos[node.n] = save

                node.keys[node.n-1] = papa.keys[position_as_child]
                papa.keys[position_as_child] = key
                return
            else:   #Mezcla
                node.keys[node.n] = papa.keys[position_as_child]
                self.merge_nodes(node, papa, papa.hijos[position_as_child + 1], 'right')


        elif papa.hijos[position_as_child-1] != [None]:     #Si tiene nodo hermano izquierdo
            if papa.hijos[position_as_child-1].n > self.t:
                print('check')
                key = papa.hijos[position_as_child-1].keys[papa.hijos[position_as_child-1].n-1]
                print(f'key = {key}')
                papa.hijos[position_as_child - 1].keys[papa.hijos[position_as_child-1].n-1] = [None]
                papa.hijos[position_as_child - 1].n -= 1

                if  papa.hijos[position_as_child - 1].hoja == 0:
                    save =  papa.hijos[position_as_child - 1].hijos[papa.hijos[position_as_child-1].n+1]
                    print('save = ', save.keys)
                    papa.hijos[position_as_child - 1].hijos[papa.hijos[position_as_child - 1].n+1] = [None]
                    node.hijos[node.n-1] = node.hijos[node.n]
                    node.hijos[node.n] = [None]

                    node.hijos.insert(0, save)
                    node.hijos.pop()


                node.keys.insert(0, papa.keys[position_as_child - 1])
                node.keys.pop()
                papa.keys[position_as_child-1] = key

            else:  # Mezcla

                node.keys[node.n] = papa.keys[position_as_child]
                self.merge_nodes(node, papa, papa.hijos[position_as_child - 1], 'left')

    def merge_nodes(self, node, papa, node_2, direction):
        if direction == 'right':
            for i in node_2.keys:
                if i != [None]:
                    node.keys[node.n] = i
                    node.n += 1
        else:

            count = 0
            for i in node_2.keys:
                if i != [None]:
                    node.keys.insert(count,i)
                    node.keys.pop()
                    node.n += 1
                    count += 1



    def check_keys(self, node):  # Metodo para saber si se cumple el orden del arbol
        keys_count = 0
        error_flag = False
        for i in node.keys:
            if i != [None]:
                keys_count += 1
        if keys_count < self.t:
            error_flag = True

        return error_flag


if __name__ == '__main__':

    print('\narbol 2')
    Pino = Arbol_B(2)
    actual = Pino.bTreeCreate()

    data = [14, 17, 18, 20, 23, 25, 27, 31, 38, 44, 48, 52, 54, 60, 80, 81, 82, 88, 21, 90,
            91]  # array con valores quese agregaran al arbol
    for i in data:  # Ciclo for para ir agregando los datos
        Pino.bTreeInsert(i)
        Pino.root.show()

    Pino.root.show()

    Pino.delete_value(23)
    Pino.root.show()

    Pino.delete_value(17)
    Pino.root.show()

    Pino.bTreeInsert(22)
    Pino.root.show()

    Pino.delete_value(90)
    Pino.root.show()

    #Pino.delete_value(80)
    Pino.root.show()