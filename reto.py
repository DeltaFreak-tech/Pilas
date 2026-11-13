from pila import Pila


def postfija(expresion: str):
    pila = Pila()
    for elemento in expresion.split():
        if elemento in "+-*/":
            b = pila.pop()
            a = pila.pop()
            if elemento == "+":
                pila.push(a + b)
            elif elemento == "-":
                pila.push(a - b)
            elif elemento == "*":
                pila.push(a * b)
            elif elemento == "/":
                pila.push(a / b)
        else:
            pila.push(int(elemento))
    return pila.pop()


def prefija(expresion: str):
    pila = Pila()
    for elemento in reversed(expresion.split()):
        if elemento in "+-*/":
            a = pila.pop()
            b = pila.pop()
            if elemento == "+":
                pila.push(a + b)
            elif elemento == "-":
                pila.push(a - b)
            elif elemento == "*":
                pila.push(a * b)
            elif elemento == "/":
                pila.push(a / b)
        else:
            pila.push(int(elemento))
    return pila.pop()


print("Postfija:", postfija("3 4 + 2 *"))
print("Prefija: ", prefija("* + 3 4 2"))
