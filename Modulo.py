from Auxiliar import Pila, Cola

class Separador: # Clase que separa elementos en una cola y una pila
    #Se llamara en le main para realizar las operaciones que se requieran
    def __init__(self):
        self.cola = Cola()
        self.pila = Pila()

    def cargar_elementos(self, elementos): # Carga los elementos en la cola
        for elemento in elementos: # Se espera que 'elementos' sea una lista de valores
            if elemento:  # Verifica que el elemento no sea vacío
                elemento = elemento.strip() # Elimina espacios en blanco al inicio y al final
            self.cola.enqueue(elemento) # Agrega el elemento a la cola

    def separar(self): # Separa los elementos en la cola y la pila
        # Alterna entre agregar a la cola y la pila según la posición del elemento
        nueva_cola = Cola() # Crea una nueva cola para almacenar los elementos en posiciones pares
        posicion = 0
        cantidad = len(self.cola.recorrer()) # Obtiene la cantidad de elementos en la cola

        for _ in range(cantidad): # Recorre la cola según la cantidad de elementos
            elemento = self.cola.dequeue() # Elimina el elemento de la cola y lo almacena en 'elemento'
            if posicion % 2 == 0: # Si la posición es par, agrega el elemento a la nueva cola
                nueva_cola.enqueue(elemento) 
            else:
                self.pila.push(elemento) # Si la posición es impar, agrega el elemento a la pila
            posicion += 1 

        self.cola = nueva_cola # Actualiza la cola con la nueva cola que contiene solo los elementos en posiciones pares

    def obtener_resultado(self): # Retorna los elementos de la cola y la pila
        if self.cola.esta_vacia() and self.pila.esta_vacia():
            raise Exception("No hay elementos en la cola o la pila.")
        return self.cola.recorrer(), self.pila
