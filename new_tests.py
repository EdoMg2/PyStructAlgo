#Meta 3.2: Proyecto Parcial 3 Implementacion de Arbol B
#EQUIPO
    #34226-LUIS MARIO VENTURA PARRA
    #33069-EDUARDO MENDOZA GOMEZ

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

    def show(self, counter=0):              #Metodo para representar el arbol B
        if counter == 0:
            print()                         #Espacio en blanco para cuando se llama por primera vez

        print(counter, str(self.keys), self.n)      # la posicion del nodo, el nodo en momento y su numero de claves

        # Recursively print the key of child nodes (if these exist).
        if self.hoja == 0:                  #Si no es hoja
            for item in self.hijos:
                try:
                    item.show(counter + 1)  #Se llamara el metodo con sus hijos
                except:
                    AttributeError


class Arbol_B:  # Clase de arboles B
    def __init__(self, gradoMimo):  # Constructor del arbolB en donde gradoMInimo sera el numero minimo de keys en un hijo y sera enviado como parametro
        self.t = gradoMimo
        self.root = [None]
        self.sucesion = []          #Atributo sucesion innecesario. Sin embargo, un error en el return del metodo de Clave siguiente, impedia el regreso de nodos a traves del metodo.

    def bTreeCreate(self):  # Metodo para crear un nuevo arbol b
        if self.root == [None]:
            self.root = Node(self.t)
        return self.root

    def bTreeSplit(self, x, i, excepcion_flag=False):
        z = Node(self.t)  # Se crea un nuevo nodo pasandole t
        y = x.hijos[i]  # copia en y el hijo en la posicion i
        if y == [None] or y == [None]:
            return
        z.hoja = y.hoja  # copia los datos de la hoja y en la nueva hoja

        for j in range(1, self.t + 1):  # for que acabara hasta el numero minimo de keys
            z.keys[j - 1] = y.keys[j + self.t]  # copia las llaves al nuevo nodo
            y.keys[j + self.t] = [None]  # borra las llaves del viejo nodo
            if z.keys[j - 1] != [None]:
                y.n -= 1                     #Se actualizan los numeros de claves de y y z
                z.n += 1
        #print(f'Y.keys = {y.keys} // Z.keys = {z.keys}')
        if y.hoja == 0:
            for j in range(1, self.t + 2):
                z.hijos[j - 1] = y.hijos[j + self.t]  # Copia los hijos al nuevo nodo
                y.hijos[j + self.t] = [None]  # Se actualiza en None
            #y.n = self.t + 1  # Actualiza el valor de n del nodo #----------------------------------------------

        if x.n == 2 * self.t:
            if z.keys[0] == [None]:
                return
            #print(f'z = {z.keys}, {z.n}')
            x.hijos.insert(i + 1, z)
            key = y.keys[y.n - 1]
            y.keys[y.n - 1] = [None]
            y.n -= 1
            count = 0
            for o in x.keys:
                if o != [None]:
                    if key > o:
                        count += 1

            x.keys.insert(count, key)
            x.keys.pop()
            x.n += 1

            (node, position_in_node, papa, position_as_child) = self.bTreeSearch(self.root, key)
            if papa == None:
                papa = Node(self.t)  # El nuevo nodo s sera la nueva raiz
                self.root = papa
                papa.hoja = 0  # Se establece que no sera un nodo hoja y que no cuenta con keys dentro
                papa.n = 0
                papa.hijos[0] = x  # Su hijo sera la antigua raiz
            #print(f'PAPA= {papa.keys}, hijo = {papa.hijos[papa.hijos.index(x)].keys}, en la posicion = {papa.hijos.index(x)}')
            self.bTreeSplit(papa, papa.hijos.index(x), True)
            # x.hijos.pop()



        else:
            #print('za')
            for j in range(x.n, i - 1, -1):  # Valores que se quedan en el nodo
                x.hijos[j + 1] = x.hijos[j]

            x.hijos[i + 1] = z  # Se actualiza el hijo en la posicion i+1
            for j in range(x.n, i - 1, -1):
                x.keys[j + 1] = x.keys[j]
                # print('entra a recorrer llaves', x.keys[j+1])
            x.keys[i] = y.keys[self.t]  # Se agrega un nuevo valor en el nodo papa
            y.keys[self.t] = [None]  # El valor asignado al papa se eliminara del hijo
            y.n -= 1  # El numero de keys disminuye
            x.n = x.n + 1
            #print(f'end: y:{y.keys}, z:{z.keys}, x = {x.keys}')

    def bTreeInsertNonFull(self, x, k, clave=False):
        i = x.n  # i sera el numero de keys en el nodo
        if x.hoja == 1 or clave == True:  # Si el nodo es hoja
            while (i >= 1) and k < x.keys[ i - 1]:  # si i es 1 o superior y al mismo tiempo la  posicion anterior en x.keys es mayor a k
                x.keys[i] = x.keys[i - 1]  # keys[i] sera la misma que el anterior
                i = i - 1  # i disminuira en uno
            if i == 0:  # Si i llega a 0
                x.keys[i] = k  # keys[i] sera k
            else:  # Si no adaptara su valor de i
                x.keys[i] = k
            x.n = x.n + 1  # El numero de keys aumentara en uno

        else:  # No es hoja

            while (i >= 1) and ( k < x.keys[i - 1]):  # de igual manera un ciclo while para encontrar la posicion en la lista de keys
                i = i - 1  # i retrocera cada vez que se cumpla la condicion del while
            # i = i+1

            # print('#i = ',i)
            # leer a disco
            if x.hijos[i] == [None]:
                x.hijos[i] = Node(self.t)

            if x.hijos[i].n == 2 * self.t and self.full_child(x.hijos[i], k) == True:  # Si el hijo en la posicion i del nodo esta lleno
                #print('perhaps')
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva
                self.bTreeSplit(x, i)
            else:
                self.bTreeInsertNonFull(x.hijos[i], k)  # Se llama de manera recursiva

    def bTreeInsert(self, k):  # Metodo que sera llamado cada vez que se agregue un nodo
        r = self.root  # r sera la raiz del arbol
        # nodo lleno
        if r.n == 2 * self.t and self.check_children(r) == True:  # Si la raiz se encuentra llena
            s = Node(self.t)  # El nuevo nodo s sera la nueva raiz
            self.root = s
            s.hoja = 0  # Se establece que no sera un nodo hoja y que no cuenta con keys dentro
            s.n = 0
            s.hijos[0] = r  # Su hijo sera la antigua raiz
            self.bTreeInsertNonFull(r, k, True)  # Se llama el metodo para insertar el nuevo valor
            self.bTreeSplit(s, s.hijos.index(r))
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
                return x, [None],papa, positionaschild  # No existe, y se regresa un None
            else:  #
                return self.bTreeSearch(x.hijos[i], k, x, i)  # Se llama el metodo de manera recursiva con el nodo hijo en la posicion ix

    def check_children(self, node):     #Metodo para verificar que los hijos no esten llenos
        if len(node.hijos) == 2 * self.t + 1:   #Si el nodo tiene
            for i in node.hijos:                #Se recorren los hijos
                if i == [None] or None:         #Si el hijo es None habra error
                    return True
                for j in range(2 * self.t):     #Se recorren las claves de cada hijo
                    if i.keys[j] == [None]:
                        return False            #Si hay un False se regresa False
            return True
        else:
            return False

    def full_child(self, node, key):
        count = 0
        for i in node.keys:
            if i != [None]:
                if key > i:
                    count += 1

        if node.hijos[count] != [None]:
            if node.hijos[count].n == 2*self.t:
                return True
        elif node.hijos[count] == [None]:
            return True

        return False

    def bTreeDelete(self, k):       #Metodo para eliminar una clave del arbol
        print(f'\nSe borrara la clave {k}...')
        (node, position_in_node, papa, position_as_child) = self.bTreeSearch(self.root, k)      #Se busca la clave, su posicion en el nodo, el nodo al que pertenece, su papa, y su posicion como hijo de ese padre
        if node == [None]:  #Si el nodo no esta en el arbol se imprime un mensaje
            print('La clave no esta presente en el arbol...')
        else:               #Si esta en el arbol...
            if node.hoja == 1:      #Si es hoja
                self.Delete_key(node, position_in_node)     #Se borra la clave
            else:       #Si no
                self.Next_key(node, position_in_node, papa) #Se busca a su sucesor
                sucesor = self.sucesion[0]          #Por meido del arreglo self.sucesion se consigue al papa y nodo del sucesor
                s_node = self.sucesion[1]
                s_papa = self.sucesion[2]

                self.keys_changer(sucesor, node, position_in_node)  #Se intercambian las claves
                node = s_node       #El nodo pasaraa a ser el del sucesor
                papa = s_papa       #El papa sera el papa del sucesor
                position_as_child = self.bTreeSearch(self.root, node.keys[0])[3]    #Por medio del search se consigue su posicion como hijo

            is_error = self.keys_checker(node)  #La variable error sera lo que devuelva el metodo keys checker
            if is_error == True and self.root != node:  #Si hay error y el nodo no es raiz (Por lo que no pasa nada si tiene menos claves que self.t)
                self.Merge_nodes(node, position_as_child, papa) #Se llama al metodo merge_nodes

    def Merge_nodes(self, node, position_as_child, papa):   #Metodo para unir nodos de un arbol

        left_brother = papa.hijos[position_as_child - 1]    #Se establecen los hermanos izquierdo y derecho del nodo
        right_brother = papa.hijos[position_as_child + 1]

        if left_brother != [None] and right_brother != [None]: #Existen ambos hermanos
            if  left_brother.n > right_brother.n:              #Si el hermano izquierdo tiene mayor cantidad de keys
                sucesor = self.Delete_key(left_brother, left_brother.n-1)   #El sucesor pasara a ser la ultima clave derecha de su hermano izquierdo
                node.keys.insert(0,papa.keys[position_as_child-1])          #Se agrega la nueva clave
                node.keys.pop()                                     #Se elimina el [None] de sobre
                papa.keys[position_as_child-1] = sucesor            #se actualiza la nueva clave del papa
                node.n += 1                                         #n aumenta
                if left_brother.hoja == 0:                          #Si el hermano no es hoja
                    node.hijos.insert(0, left_brother.hijos[left_brother.n])        #Se reacomodan sus hijos a los del nodo
                    node.hijos.pop(len(node.hijos)-1)
                    left_brother.hijos.pop(left_brother.n)
                    left_brother.hijos.append([None])

            elif right_brother.n > self.t:                      #El hermano derecho tiene de sobra
                sucesor = self.Delete_key(right_brother, 0)     #Se consigue el sucesor como la primer clave del hermano derecho
                node.keys[node.n] = papa.keys[position_as_child]   #Se actualizan las claves del papa y nodo
                papa.keys[position_as_child] = sucesor
                node.n += 1                             #n aumenta en el nodo
                if right_brother.hoja == 0:                     #Si el hermano derecho no es hoja
                    node.hijos.insert(node.n, right_brother.hijos[0])   #Se pasan los hijos del hermano a los del nodo inicial
                    node.hijos.pop()
                    right_brother.hijos.pop(0)
                    right_brother.hijos.append([None])

            else:                                               #Ninguno de los hermanos instantaneos tiene claves de sobra
                self.Merge_assist(node, right_brother, papa, position_as_child, 'right')    #Si ninguno de los hermanos tiene claves de sobra   Se llama el metodo Merge_assist


        elif right_brother != [None]:   #Existe un unico hermano derecho
            if right_brother.n > self.t:                        #Si el hermano derecho tiene nodos de sobra, se repite igual que en el caso de que ambos hermanos existan
                sucesor = self.Delete_key(right_brother, 0)
                node.keys[node.n] = papa.keys[position_as_child]
                papa.keys[position_as_child] = sucesor
                node.n += 1
                if right_brother.hoja == 0:                     #Se reasignan los hijos del hermano derecho si es que tiene
                    node.hijos.insert(node.n, right_brother.hijos[0])
                    node.hijos.pop()
                    right_brother.hijos.pop(0)
                    right_brother.hijos.append([None])

            else: #Ninguno de los hermanos instantaneos tiene claves de sobra
                self.Merge_assist(node, right_brother, papa, position_as_child, 'right')    #Se llama



        elif left_brother != [None]:    #Existe un unico hermano izquierdo
            if left_brother.n > self.t: #Si tiene hermanos de sobra
                sucesor = self.Delete_key(left_brother, left_brother.n - 1) #Al igual que en los casos anteriores se reacomodan las nuevas claves del papa y el nodo
                node.keys.insert(0, papa.keys[position_as_child - 1])
                node.keys.pop()
                papa.keys[position_as_child - 1] = sucesor
                node.n += 1         #n aumenta en uno
                if left_brother.hoja == 0:                          #Si el hermano no es hoja
                    node.hijos.insert(0, left_brother.hijos[left_brother.n])        #Se reacomodan sus hijos a los del nodo
                    node.hijos.pop(len(node.hijos)-1)
                    left_brother.hijos.pop(left_brother.n)
                    left_brother.hijos.append([None])
            else:                           #Si no se llama el metodo de soporte
                self.Merge_assist(node, left_brother, papa, position_as_child, 'left')

    def Merge_assist(self, node, brother, papa, position_as_child, direction_brother):      #Metodo para asistir en la union de nodos

        if direction_brother == 'right':            #Si la direccion con la que se envio es derecha

            node.keys[node.n] = papa.keys[position_as_child]    #Su ultima clave pasara a aser la del papa
            node.n += 1                             #El numero de claves aumentara en uno
            for i in brother.keys:                  #Se recorren las claves del hermano
                if i != [None]:
                    node.keys[node.n] = i           #Se le pasan las claves que no sean [None] y su numero de keys aumenta
                    node.n += 1
            for i in range(position_as_child+1, len(papa.hijos)): #Se recorreran las posiciones de los hijos del papa
                if papa.hijos[i] != [None]:
                    papa.hijos[i] = papa.hijos[i+1]
            save = self.Delete_key(papa, position_as_child)            #Se borrara la clave del padre

        else:       #Si direccion = 'left'

            brother.keys[brother.n] = papa.keys[position_as_child-1]   #El hermano tendra la clave del papa
            brother.n += 1              #n aumenta
            for i in node.keys:         #Se pasaran las claves del nodo al hermano
                if i != [None]:
                    brother.keys[brother.n] = i
                    brother.n += 1      #n del hermano aumenra

            save = papa.keys[position_as_child - 1]
            papa.keys[position_as_child - 1] = [None]       #Se elimina la clave del papa y su hijo en el que estaba el nodo inicial es [None]
            papa.hijos[position_as_child] = [None]
            papa.n -= 1                                     #El tamano del papa se actualiza

        if self.keys_checker(papa) == True and self.root != papa:  # Si hay error en el nodo papa
            if self.t == 1:     #Medidas para cuando sea un arbol con t= 1
                papa.keys[0] = save
            # Se buscara el padre del padre y su posicion como papa
            (papa, position_in_node, grandpa, position_as_grandson) = self.bTreeSearch(self.root, papa.keys[0])
            left_u = grandpa.hijos[position_as_grandson - 1]  # Se crean los tios izquierdos y derechos
            right_u = grandpa.hijos[position_as_grandson + 1]
            if self.t == 1:
                papa.keys[0] = [None]
            print('a')
            if right_u != [None]:  # Si hay tio derecho
                print('b')
                if right_u.n > self.t or self.t == 1:  # Si los numero de claves del tio erecho es mayor al minimo
                    print('c')
                    self.Merge_nodes(papa, position_as_grandson, grandpa)  # Se llama el metodo merge
                else:  # Si no se llamara el metodo para reducir un nivel
                    print('d')

                    self.Merge_lvl_down(papa, right_u, grandpa, 'right')

            elif left_u != [None]:  # Si existe un hermano izquierdo
                print('e', left_u.keys, node.keys)
                if left_u.n > self.t or self.t == 1:  # Si tiene claves de sobra
                    print('f')
                    self.Merge_nodes(papa, position_as_grandson, grandpa)  # Se llama el metodo merge para unirlo con su hermano
                else:
                    print('g')

                    self.Merge_lvl_down(papa, left_u, grandpa, 'left')  # Si no tiene de sobra se llama el metodo para bajar un nivel

        elif self.root == papa:  # Si la raiz es el padre
            if papa.n == 0:  # Y si no le quedan claves
                self.root = papa.hijos[papa.n]  # La nuevo raiz sera su unico hijo

    def Merge_lvl_down(self, merged_node, brother, papa, direction_brother):    #Metodo fusionar al papa con sus hijos
        if direction_brother == 'right':        #Si la direccion es derecha
            for i in range(self.t-1):           #for para agregar ir agregando los nodos de su padre
                merged_node.keys[merged_node.n] = papa.keys[i]
                merged_node.n += 1              #se actualiza n
            count = self.t                      #contador
            for i in brother.keys:              #Se recorren las claves del hermano
                if i != [None]:
                    merged_node.keys[merged_node.n] = i     #Se agregan las claves del hermano al nodo y n aumenta
                    merged_node.n += 1
            for i in brother.hijos:                         #Se agregan los hijos del hermano
                if i != [None]:
                    merged_node.hijos[count] = i
                    count += 1

            papa.keys = merged_node.keys                    #El papa pasara a adquirir todos los valores que adquirio el nodo original
            papa.hijos = merged_node.hijos
            papa.n = merged_node.n
        else:                                               #Si la direccion fue derecha
            count = 0
            for i in range(self.t-1):                       #Se agregan las claves del papa en sus posiciones correespondientes del nodo
                merged_node.keys.insert(count,papa.keys[i])
                merged_node.n += 1
                merged_node.keys.pop()
                count += 1
            count = 0               #Count se reinicia
            for i in brother.keys:                          #SE agregan las claves del hermano a sus nuevas posiciones
                if i != [None]:
                    merged_node.keys.insert(count, i)
                    merged_node.keys.pop()
                    merged_node.n += 1
                    count += 1
            count = 0              #Count se reinicia
            for i in brother.hijos:                         #Se recorren los hijos del hermano
                if i != [None]:
                    merged_node.hijos.insert(count, i)      #Se le insertan los hijos del hermano
                    count  += 1

            papa.keys = merged_node.keys                    #El papa pasara a adquirir los valores que su hijo estuvo adquiriendo
            papa.hijos = merged_node.hijos
            papa.n = merged_node.n

    def Delete_key(self, node, position_in_node):   #Metodo para borrar una clave
        save = node.keys.pop(position_in_node)      #Save sera la posicion que se eliminara
        node.keys.append([None])
        node.n -= 1     #El tamano del nodo disminuye

        return save     #Se regresa el save

    def Next_key(self, node, position_in_node, papa, direction = None): #Metodo para conseguir la clave sucesora de un nodo
        if node.hoja == 1: #Si es hoja
            if direction == 'left':     #Si la direccion enviada es izquierda
                sucesor = self.Delete_key(node, node.n-1)   #Se borrara el ultimo valor del nodo
            else:                       #Si es derecho
                sucesor = self.Delete_key(node, 0)          #Se borrara el primer valor

            self.sucesion = [sucesor, node, papa]           #Se regresan los valores del sucesor por medio del atributo sucesion
            return sucesor

        else:              #Si no es hoja
            if direction == 'left':                         #Si se envia la direccion izquierda
                self.Next_key(node.hijos[node.n], position_in_node, node, 'left')       #Se llama de manera recursiva con los nodos correspondientes
            elif direction == 'right':                                                  #Igualmente con la direccion derecha
                self.Next_key(node.hijos[0], position_in_node, node, 'right')
            else:               #Si se llamo por primera vez...
                if node.hijos[position_in_node] != [None] and node.hijos[position_in_node+1] != [None]: #Se elige el hijo con mayor claves
                    if  node.hijos[position_in_node].n >= node.hijos[position_in_node+1].n:             #Si tiene un hijo izquierdo con mas hijos
                        self.Next_key(node.hijos[position_in_node], node.hijos[position_in_node].n-1, node, 'left')     #Se llama recursivamente con el hijo izquierdo
                    else:
                        self.Next_key(node.hijos[position_in_node+1],  node.hijos[position_in_node].n, node, 'right')   #Si no se llama con el hijo derecho

                elif node.hijos[position_in_node] != [None]:                                            #Si solo tiene hijo izquierda
                    self.Next_key(node.hijos[position_in_node], node.hijos[position_in_node].n - 1, node, 'left')       #Se llama con el hijo izquierdo

                else:                                                                                  #Si no con el hijo derecho
                    self.Next_key(node.hijos[position_in_node + 1], 0, node, 'right')

    def keys_changer(self, sucesor, node, position_in_node):    #Metodo para cambiar valores de claves entre dos nodos
        node.keys[position_in_node] = sucesor

    def keys_checker(self, node):           #Metodo para verificar que no haya un numero menor al minimo de claves dentro de un nodo
        if node.n < self.t:                 #Si el nodo tiene menos claves que
            return True                     #Se devuelve True
        for i in range(node.n):             #Si tiene un [None] dentro de las claves se devuelve True
            if node.keys[i] == [None]:
                return True


        return False                        #Si no solo se devuelve False

if __name__ == '__main__':

    print('\n**** PROYECTO FINAL ESTRUCTURA DE DATOS ****')

    Pino = Arbol_B(1)
    actual = Pino.bTreeCreate()
    print('\n--- INSERCIONES ---')
    #SE hace un arreglo de los numeros que se agregaran al arbol B
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # array con valores quese agregaran al arbol
    for i in data:  # Ciclo for para ir agregando los datos
        print(f'\n--Se agregara la clave: {i}')
        Pino.bTreeInsert(i)
        Pino.root.show()

    print('\n--- BORRADOS ---')

    borrados = [5, 4, 9, 15, 16, 6, 17, 12, 10, 1, 8, 3, 14, 11, 20, 2, 19, 7, 13, 18]
    for j in borrados:
        Pino.bTreeDelete(j)
        Pino.root.show()


    #RETROALIMENTACION
        #LUIS
    #Durante nuestra estancia en la clase de Estructura de datos pasé por muchas emociones. Al principio todo me parecía complicado, tardado e innecesario.
    #Con el tiempo comprendí que era una clase de algoritmos y métodos muy bien estructurada, lo que me permitió darle otro enfoque y encontrarle el lado interesante.
    #Me dirigí hacia la maestra y le comenté lo que sucedía, la cuál resultó siendo muy comprensible y amistosa, lo que provocó cierto afecto de mi parte; ella accedió sin objeción a ayudarme,
    #cosa que fue decisiva para mí compresión a futuro. La organización de las clases me parecían agradables, no llegaba al punto de ser agobiante ni repetitiva, creando un mejor ambiente para aprender.
    #Los proyectos eran desafiantes cosa que era buena a principio, sin embargo considero que es necesario un poco más de retroalimentación. Al final del semestre me voy con una experiencia más que gratificante
    #y satisfecho de lo que logré y aprendí durante este curso.

        #Eduardo
    #En un principio habia notado una enorme diferencia entre el nivel de conocimiento necesario para esta clase y el que era necesario para la clase de programacion orientada a objetos. En lo personal
    #me sentia bastante perdido en el uso de cosas tan basicas como los arrays y funciones unicas de python. Con suerte, con el avance del semestre y las explicaciones de los temas, fui aclarando mis dudas
    #poco a poco. Me agrado mucho la forma en que los temas se fueron interconectando, debido a que todo lo que se ha aparendido se ha vuelto a utilizar de una u otra forma en los siguientes temas
    #que se fueron presentando. La utilizacion de diferentes herramientas tecnologicas para la facilitacion del tema, y posteriormente a partir de un pseudocodigo ser capaces de crear nuestro codigo
    #con las distintas caracteristicas elegidas por cada alumno fueron bastantes importantes para mi ritmo de aprendizaje. Por ultimo, terminando este semestre me voy con un aumento en mis conocimientos de
    #programacion, y me siento realizado por haber comprendido todos los temas de la materia.


    # ULTIMA MODIFICACION 26 DE NOVIEMBRE DEL 2021 A LAS 12:10 PM, TIJUANA BAJA CALIFORNIA
