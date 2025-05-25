class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.esta_vacia():
            raise Exception("Pila vacía")
        valor = self.cima.valor
        self.cima = self.cima.siguiente
        return valor

    def peek(self):
        if self.esta_vacia():
            return None
        return self.cima.valor

    def esta_vacia(self):
        return self.cima is None

    def imprimir(self):
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

    def enqueue(self, valor):
        nuevo = Nodo(valor)
        if self.final:
            self.final.siguiente = nuevo
        self.final = nuevo
        if self.frente is None:
            self.frente = nuevo

    def dequeue(self):
        if self.esta_vacia():
            raise Exception("Cola vacía")
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def esta_vacia(self):
        return self.frente is None

    def recorrer(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos
