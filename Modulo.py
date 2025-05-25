from Auxiliar import Pila, Cola

class Separador:
    def __init__(self):
        self.cola = Cola()
        self.pila = Pila()

    def cargar_elementos(self, elementos):
        for elemento in elementos:
            self.cola.enqueue(elemento)

    def separar(self):
        nueva_cola = Cola()
        posicion = 0
        cantidad = len(self.cola.recorrer())

        for _ in range(cantidad):
            elemento = self.cola.dequeue()
            if posicion % 2 == 0:
                nueva_cola.enqueue(elemento)
            else:
                self.pila.push(elemento)
            posicion += 1

        self.cola = nueva_cola

    def obtener_resultado(self):
        return self.cola.recorrer(), self.pila
