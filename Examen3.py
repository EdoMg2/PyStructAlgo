#Practica 3.2 EXAMEN PARCIAL 3

    #Lee con atención el problema que se plantea, y realiza un programa en Python que dé solución por medio de programación (Clases, Métodos e impresiones). Y muestra la imagen del Grafo resultante.

#33069-EDUARDO MENDOZA GOMEZ

import networkx as nx           #Librerias necesarias para la visualizacion del grafo
import matplotlib.pyplot as plt # Dibuje imágenes y fotos que muestren paquetes y oraciones

class Vertex(): #Clase de vertices
    def __init__(self, n):          #constructor de los parametros nombre y vecinos
        self.name = n
        self.neighbors = list()         #vecinos es una lista
        self.color = 'White'            #color del vertice
        self.d = 0                      #t. descubrimiento
        self.p = None                   #predecesor
        self.distance = None            #distancia
        self.f = 0                      #Tiempo de termino
        self.gi = 0                     #grado de entrada
        self.go = 0                     #grado de salida
    def add_neighbor(self, v):         #Metodo para agregar a un vertice vacio
        if v not in self.neighbors:     #Si el parametro enviado no se encuentra en vecinos
            self.neighbors.append(v)    #Se agrega v y se ordena la lista
            self.neighbors.sort()



class Grafo():              #Clase de grafos
    def __init__(self):
        self.vertices = {} #El constructor solo creara el indice de vertices
        self.time = 0

    def add_Vertex(self, vertex): #Metodo para anadir un vertice
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices: #Se necesita que el parametro vertex sea una instancia Vertex() y que no sea un valor repetido
            self.vertices[vertex.name] = vertex                             #Se asigna la posicion del nuevo vertice en el indice de vertices
            return True
        else:
            return False                                                    #Si no se envia correctamente se regresa un False

    def add_double_Edge(self, u, v): #Metodo para agregar una conexion mutua entre dos vertices
        if u in self.vertices and v in self.vertices:   #Los vertices u y v deberan estar dentro de los vertices del grafo
            for key, value in self.vertices.items():    #Se busca u o v y se envia el otro vertice dentro de su lista de vecinos
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True                                 #Si el procedimiento fue efectivo se regresa un True
        else:
            return False                                #De lo contrario se regresa un False

    def add_Edge(self, u, v):       #Metodo para agregar solo una conexion
        if u in self.vertices and v in self.vertices:   #Al igual que en el metodo anterior u y v deberan de ser objetos Vertex
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                    v = self.vertices[v]
                    u = self.vertices[u]
                    v.gi += 1                           #Cuando se agregue una arista, el grado de entrada de del destino aumenta, y el de salida del vertice de donde salio aumenta
                    u.go += 1
                #if key == v:                           #La unica diferencia es que u no se agregara a ala lista de vecinos de v
                    #value.add_neighbor(u)
            return True
        else:
            return False

    def print_Grafo(self):          #Metodo para imprimir el grafo
        for key in sorted(list(self.vertices.keys())):  #Se iran recorriendo los vertices del grafo junto a los vertices que tiene como vecino.
            print(f"EMPLEADO: {key}, DOMINA A: {str(self.vertices[key].neighbors)} // Es dominado por un total de = {self.vertices[key].gi} empleados, y domina a un total de = {self.vertices[key].go} empleados //")

    def BFS(self, s): #Metodo para el recorrido BFS
        for i in self.vertices: #Se recorren todos los vertices dentro del grafo para reinciar sus parametros color, p, y t
            i = self.vertices[i]
            i.color = 'White'
            i.p = None
            i.f = 0
            i.d = 0
        if s in self.vertices:      #Si es es un vertice dentro del grafo se cumplira
            s = self.vertices[s]    #s sera el vertice del grafo
            s.color = 'Gray'        #El color de s sera gray y sus demas atributos seran los prestablecidos
            s.d = 0
            s.p = None
            Q = list()              #Se crea la lista Q y se le agrega el vertice s
            Q.append(s)
            while len(Q) != 0:      #Mientras Q tenga elementos...
                u = Q.pop()         #Se borrara un elemento de q y sera asignado a la variable u
                for v in u.neighbors:   #Se recorre por el vertice v los vectores adyacentes de u
                    v = self.vertices[v]
                    if v.color == 'White':  #Si el color que se encuentra es blanco cambiara a gris
                        v.color = 'Gray'
                        v.d = u.d + 1       #Su tiempo aumenta en el del anterior + 1 y su vector predecesor sera u
                        u.p = u
                        Q.append(v)         #Se agrega v a la lista Q
                u.color = 'Black'           #El color de u sera negro
            return True
        else:                      #Si no es un vertice se regresara un False
            return False

    def DFS(self, s):           #Metodo del recorrido DFS, que recibira al vertice s como parametro
        self.t = 0
        for i in self.vertices: #Se recorren todos los vertices dentro del grafo para reinciar sus parametros color, p, y t
            i = self.vertices[i]
            i.color = 'White'
            i.p = None
            i.f = 0
            i.d = 0
        if s in self.vertices:      #Si es es un vertice dentro del grafo se cumplira
           s = self.vertices[s]
           for u in self.vertices:  #Se recorren los vertices del arbol y se llama el metodo auxiliar si el color del vertice es blanco
               u = self.vertices[u]
               if u.color == 'White':
                   self.DFS_VISITAR(u)

    def DFS_VISITAR(self, u): #Metodo complementario del recorrido DFS
        self.time += 1        #El tiempo del grafo aumentara en uno
        u.d = self.time       #El tiempo 0 del vertice sera el tiempo con el que primeramente se llamo al metodo
        u.color = 'Gray'      #Su color pasara a ser gris
        for v in u.neighbors:           #Se recorren los nodos adyacentes de v
            v = self.vertices[v]
            if v.color == 'White':      #Si el nodo recorrido es blanco se reasigna su predecesor y se llama recursivamente el metodo
                v.pred = u
                self.DFS_VISITAR(v)
        u.color = 'Black'               #Al final de recorrer a sus vecinos, pasara a ser negro
        self.time += 1                  #El tiempo aumenta en  1
        u.f = self.time                 #Se asigna su tiempo final

    def Create_matrix(self):            #Metodo para crear una matriz
        fil = len(self.vertices)        #El numero de filas y columnas sera el numero de vertices que el grafo contenga
        col = len(self.vertices)
        matrix = [[0 for i in range(fil)] for j in range(col)]      #Se crea una matriz cuadrada con el numero de filas y columnas llena de ceros

        #Contadores de apoyo
        count1 = 0
        count2 = 0
        count = 0

        for i in self.vertices:         #Se recorren todos los vertices dentro del grafo
            count1 = 0                  #Se reinciia el contador 1
            i =self.vertices[i]
            for k in self.vertices:     #Se vuelven a recorrer los vertices
                k = self.vertices[k]    #se asigan un vertice a k
                if k.name in i.neighbors:           #Si k esta dentro de los vertices de adyacencia de i
                    matrix[count2][count1] = 1          #la posicion que le toca en la matriz sera un uno
                count1 +=1                              #Los contadores aumentan en 1 con cada iteracion del ciclo for
            count2 += 1

        b = []                                      #Se crea una matriz de apoyo
        for i in self.vertices:                     #Se le agregan los nombres de los vertices
            b.append(i)

        print('*** MATRIZ con lasa iniciales de los empleados....')
        print(' ', end= ' ')
        for v in self.vertices:
            print(f' {v[:1]}', end = ' ')           #Se una ilera con las inciales o numero de cada vertice de la amtriz
        print()
        for a in matrix:                            #Se imprime la matriz con una primera columna con el nombre de cada vertice
            print(b[count][:1], a)
            count += 1

    def conseguir_lider(self, vertice):     #Metodo para conseguir el lider en el problema del examen
        vertice = self.vertices[vertice]    #Se empezara por el primer vertice del grafo
        lider = vertice                     #El lider sera el vertice desde que se llamo el metodo
        lideres = [lider]                   #Los lideres seran los vertices mayores al grafo
        for i in self.vertices:             #Se recorren los vertices del grafo
            i = self.vertices[i]
            if i.gi <= lider.gi and i.go >= lider.go:       #Si el grado de enbtrada del vertice en momento es menor que el del lider y su grado de salida es mayor
                if lider  != i:
                    lider = i                               #El lider pasara a ser el vertice nuevo
                    lideres.append(lider)                   #Se le agreega el vertice a la lista de lideres


        for i in range (1, len(lideres)):                   #Se recorren los lideres en el orden que fueron agregados
            if lideres[i].go > lideres[i-1].go or lideres[i].gi < lideres[i-1].gi:     #Si un lider tiene un grado de entrada o salida mayor o menor que el que le sigue se eliminara de la lista
                lideres.pop(i-1)

        print('El/Los lideres calculados son: ')                                        #Se imprimen el/los lideres del grafo
        for v in lideres:
            print(f' {v.name}', end=' ')
        print('\n')

if __name__ == '__main__':


    G = Grafo()         #Se crea la instancia G como un grafo
    vertices = ['Alejandra', 'Beatriz', 'Cesar', 'Dania', 'Ernesto']  #Por medio de un ciclo for se iran agregando vertices al grafo c con los numeros dentro del array vertices
    for i in vertices:
        G.add_Vertex(Vertex(i))
    print('\n*** EXAMEN PRACTICO #3 ***\n')

    G.add_Edge('Alejandra', 'Beatriz')      #Se crean las conexiones unidireccionales entre los vertices manualmente
    G.add_Edge('Alejandra', 'Cesar')
    G.add_Edge('Alejandra', 'Dania')
    G.add_Edge('Beatriz', 'Dania')
    G.add_Edge('Cesar', 'Ernesto')
    G.add_Edge('Cesar', 'Beatriz')
    G.add_Edge('Dania', 'Alejandra')
    G.add_Edge('Dania', 'Cesar')
    G.add_Edge('Dania', 'Ernesto')
    G.add_Edge('Ernesto', 'Alejandra')
    G.add_Edge('Ernesto', 'Beatriz')

    G.Create_matrix()           #Se crea e imprime una matriz con los valores del grafo imprimiendo las iniciales de los nombres


    grafo = nx.DiGraph()              #Se crea el objeto grafo utilizando la libreria networkx
    for key in sorted(list(G.vertices.keys())):         #Doble ciclo for para agregar las conexiones de cada vertice y sus vertices adyacentes del grafo G
        #print(key, str(G.vertices[key].neighbors))
        for j in G.vertices[key].neighbors:
            grafo.add_edges_from([(key, j)])            #Se le agrega key (vertice), y j(vecino)

    print('\n*** Representacion de listas de adyaciencia + Grados de entrada y salida de cada vertice ***\n')
    G.print_Grafo()

    print('\n*** LLAMANDO AL METODO PARA CCONSEGUIR AL LIDER DEL GRAFO DE 5 VERTICES ***\n')
    G.conseguir_lider('Alejandra')      #SE llama con el primer grafo como inicio
    print('EL lider de grupo se consiguio mediante los atributos de grado de entrada y salida de vertice que fueron anadidos en este proyecto, a traves del metodo conseguir_lider, se recorrieron todos los vertices del grafo y se obtuvo el/los vertices con mas salidas y menos entradas a la vez')

    nx.draw(grafo, with_labels=True)    #Se dibuja el grafo por medio de la libreria nx.draw



    print('-Cargando grafo...')     #Se mostrara en pantalla la representacion del grafo

    plt.show()

    # ULTIMA MODIFICACION 25 DE NOVIEMBRE DEL 2021 A LAS 12:10 PM, TIJUANA BAJA CALIFORNIA