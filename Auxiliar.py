class Nodo: # Clase para representar un nodo que se usara en la Pila y en la Cola
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor): # Agrega un elemento a la cima de la pila
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self): # Elimina y retorna el elemento en la cima de la pila
        if self.esta_vacia():
            raise Exception("Pila vacía")
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def peek(self): # Retorna el elemento en la cima de la pila sin eliminarlo
        if self.esta_vacia():
            return None
        return self.cima.valor

    def esta_vacia(self): # Verifica si la pila está vacía
        return self.cima is None

    def imprimir(self): # Imprime los elementos de la pila
        elementos = []
        actual = self.cima
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print(elementos)

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def enqueue(self, valor): # Agrega un elemento al final de la cola
        nuevo = Nodo(valor)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if self.frente is None:
            self.frente = nuevo

    def dequeue(self):# Elimina y retorna el elemento al frente de la cola
        if self.esta_vacia():
            raise Exception("Cola vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def esta_vacia(self): # Verifica si la cola está vacía
        return self.frente is None

    def recorrer(self): # Retorna una lista con los elementos de la cola
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
