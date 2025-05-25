from Modulo import Separador

def validar_entrada(cadena):
    elementos = cadena.split(',')
    lista_valores = []
    for elem in elementos:
        valor = elem.strip()
        if valor == '':
            continue
        lista_valores.append(valor)
    return lista_valores

if __name__ == "__main__":
    while True:
        print("Separador de elementos con Pila y Cola")
        entrada = input("Ingrese los elementos separados por coma (escribir break para salir): ")
        if entrada.lower() == 'break':
            print("Saliendo del programa.")
            break
        elementos = validar_entrada(entrada)

        if not elementos:
            print("No se ingresaron elementos válidos.")
        else:
            separador = Separador()
            separador.cargar_elementos(elementos)
            separador.separar()

            cola_resultado, pila_resultado = separador.obtener_resultado()

            print(f"Cola (posiciones pares): {cola_resultado}")
            print("Pila (posiciones impares): ", end="")
            pila_resultado.imprimir()
            print("\n")
