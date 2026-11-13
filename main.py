from pila import Pila


def menu():
    pila = Pila()

    while True:
        print("MENÚ DE OPCIONES DE LA PILA")
        print("1. Push")
        print("2. Pop")
        print("3. Mostrar pila")
        print("4. Verificar si está vacía")
        print("5. Calcular promedio")
        print("6. Tamaño de la pila")
        print("7. Buscar un elemento")
        print("8. Obtener elemento del tope (Peek)")
        print("9. Limpiar la pila")
        print("10. Invertir pila (Método personal)")
        print("11. Salir")

        opcion = input("Selecciona una opción del menú: ")

        match opcion:
            case "1":
                try:
                    valor = int(input("Ingresa un número entero: "))
                    pila.push(valor)
                    print(f"-> Elemento {valor} apilado con éxito.")
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")

            case "2":
                resultado = pila.pop()
                if resultado == "Error.Underflow":
                    print(
                        "-> Error: La pila está vacía (Underflow), no se puede desapilar."
                    )
                else:
                    print(f"-> Elemento extraído: {resultado}")

            case "3":
                pila.imprimir()

            case "4":
                if pila.is_empty():
                    print("-> La pila está VACÍA.")
                else:
                    print("-> La pila si tiene elementos.")

            case "5":
                res_promedio = pila.promedio()
                if res_promedio == "Error.Underflow":
                    print(
                        "-> Error: La pila está vacía, no se puede calcular el promedio."
                    )
                else:
                    print(f"-> El promedio de los elementos es: {res_promedio:.2f}")

            case "6":
                print(
                    f"-> El tamaño actual de la pila es de {pila.tamano()} elementos."
                )

            case "7":
                try:
                    valor_buscado = int(input("Ingresa el número a buscar: "))
                    if pila.buscar(valor_buscado):
                        print(
                            f"-> El elemento {valor_buscado} si se encuentra en la pila."
                        )
                    else:
                        print(
                            f"-> El elemento {valor_buscado} no se encuentra en la pila."
                        )
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")

            case "8":
                tope = pila.peek()
                if tope == "Error.Underflow":
                    print("-> Error: La pila está vacía, no hay elemento en el tope.")
                else:
                    print(f"-> El elemento en el tope es: {tope}")

            case "9":
                pila.limpiarpila()
                print("-> La pila ha sido limpiada.")

            case "10":
                if pila.is_empty():
                    print("-> La pila está vacía, no hay elementos para invertir.")
                else:
                    pila.invertir()
                    print("-> Se ha invertido el orden de la pila.")

            case "11":
                print("Adios! Gracias por usar el programa.")
                break

            case _:
                print("Opción inválida. Intentalo de nuevo.")


if __name__ == "__main__":
    menu()
