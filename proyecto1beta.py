class Pila:
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
    def insertar(self, item):
        if self.esta_llena() == False:
            # Se agrega el valor deseado en la ultima posicion
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
            print('La pila esta vacia...')
            return False
        # Si contiene un valor se extrae el ultimo que fue agregado
        else:
            # Se saca el ultimo de la fila
            save = self.lista.pop(self.top)
            # Se guarda el valor extraido en caso de ser necesario
            self.top -= 1
        # Se regresa el valor guardado
        return save

    # Metodo para identificar el valor maximo en la lista
    def verificar(self):
        if self.esta_vacia() == True:
            print('La pila esta vacia...')
            return False
        else:
            open_list = ["[", "{", "("]
            close_list = ["]", "}", ")"]
            stack = Pila(10)
            j = 0
            for i in self.lista:
                j += 1
                if i in open_list:
                    stack.insertar(i)
                elif i in close_list:
                    pos = close_list.index(i)
                    if (stack.top > -1) and (open_list[pos] == stack.lista[stack.top]):
                        stack.extraer()
                    else:
                        return j
                        break
            if stack.top == -1:
                return 'Success'
            else:
                return j

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
        # Se regresa el valor guardado
        return save

prueba = '{'
prueba_pila = Pila(10)
for i in range(len(prueba)):
    prueba_pila.insertar(prueba[i])

print(prueba_pila.verificar())
