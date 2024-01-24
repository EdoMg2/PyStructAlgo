#Practica 3.2 Recorridos-Grafo
#Sube tu programa para el recorrido DFS - y el ejemplo de diskstra visto en clase
#EQUIPO
    #34226-LUIS MARIO VENTURA PARRA
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
                #if key == v:                           #La unica diferencia es que u no se agregara a ala lista de vecinos de v
                    #value.add_neighbor(u)
            return True
        else:
            return False

    def print_Grafo(self):          #Metodo para imprimir el grafo
        for key in sorted(list(self.vertices.keys())):  #Se iran recorriendo los vertices del grafo junto a los vertices que tiene como vecino.
            vertice_color = self.vertices[key].color
            print(f"Vertice: {key}, Color: {vertice_color}, Vecinos: {str(self.vertices[key].neighbors)} , Tiempo0: {self.vertices[key].d}, Tiempo1: {self.vertices[key].f}")

    def BFS(self, s): #Metodo para el recorrido BFS
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
        for i in self.vertices: #Se recorren todos los vertices dentro del grafo para reinciar sus parametros color y p
            i = self.vertices[i]
            i.color = 'White'
            i.p = None
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

if __name__ == '__main__':


    G = Grafo()         #Se crea la instancia G como un grafo
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  #Por medio de un ciclo for se iran agregando vertices al grafo c con los numeros dentro del array vertices
    for i in vertices:
        G.add_Vertex(Vertex(i))
    print('\n*** Grafo #1 ***\n')

    G.add_double_Edge('A', 'B')      #Se crean las conexiones dobles entre los vertices manualmente
    G.add_double_Edge('A', 'E')
    G.add_double_Edge('B', 'F')
    G.add_double_Edge('E', 'D')
    G.add_double_Edge('H', 'D')

    G.add_double_Edge('E', 'H')
    G.add_double_Edge('F', 'I')
    G.add_double_Edge('F', 'J')
    G.add_double_Edge('G', 'F')
    G.add_double_Edge('G', 'C')





    G.print_Grafo()             #Se imprime la forma en que quedo el grafo


    grafo = nx.Graph()              #Se crea el objeto grafo utilizando la libreria networkx
    for key in sorted(list(G.vertices.keys())):         #Doble ciclo for para agregar las conexiones de cada vertice y sus vertices adyacentes del grafo G
        #print(key, str(G.vertices[key].neighbors))
        for j in G.vertices[key].neighbors:
            grafo.add_edges_from([(key, j)])            #Se le agrega key (vertice), y j(vecino)



    print('\n*** RECORRIDO DFS Grafo #1 desde el numero 1***\n')



    nx.draw(grafo, with_labels=True)
    G.DFS('A')
    G.print_Grafo()

    print('-Cargando grafo #1...')

    plt.show()

    # ULTIMA MODIFICACION 24 DE NOVIEMBRE DEL 2021 A LAS 12:10 PM, TIJUANA BAJA CALIFORNIA
