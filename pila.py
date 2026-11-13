class Pila:

    class Nodo:
        def __init__(self, info: int):
            self.info = info
            self.sig = None

    def __init__(self):
        self.tope = None

    def push(self, dato: int):
        """Agregar un elemento en la cima de la pila (Push)"""
        nuevo = self.Nodo(dato)
        nuevo.sig = self.tope
        self.tope = nuevo

    def is_empty(self) -> bool:
        """Devuelve True si la pila está vacía, False en caso contrario"""
        return self.tope is None

    def pop(self) -> int | str:
        """Extrae y retorna el elemento de la cima (Pop)"""
        if self.is_empty():
            return "Error.Underflow"

        informacion = self.tope.info
        self.tope = self.tope.sig
        return informacion

    def promedio(self) -> float | str:
        if self.is_empty():
            return "Error.Underflow"

        suma = 0
        contador = 0
        reco = self.tope
        while reco is not None:
            suma += reco.info
            contador += 1
            reco = reco.sig

        return suma / contador

    def tamano(self) -> int:
        contador = 0
        reco = self.tope
        while reco is not None:
            contador += 1
            reco = reco.sig
        return contador

    def buscar(self, valor: int) -> bool:
        reco = self.tope
        while reco is not None:
            if reco.info == valor:
                return True
            reco = reco.sig
        return False

    def peek(self) -> int | str:
        if self.is_empty():
            return "Error.Underflow"
        return self.tope.info

    def limpiarpila(self) -> None:
        self.tope = None

    def invertir(self) -> None:
        if self.is_empty():
            return

        pila_auxiliar = Pila()

        # Desapilar de la pila actual y apilar en la auxiliar para invertir el orden
        while not self.is_empty():
            pila_auxiliar.push(self.pop())

        # Asignar la referencia del tope de la auxiliar a la principal
        self.tope = pila_auxiliar.tope

    def imprimir(self) -> None:
        if self.is_empty():
            print("\n[Pila vacía]")
            return

        print("\n--- Estado de la Pila (Cima -> Fondo) ---")
        reco = self.tope
        while reco is not None:
            print(f"| {reco.info} |")
            reco = reco.sig
        print("---------")
