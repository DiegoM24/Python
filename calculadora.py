#Definir funcion
def sumar(a, b):
    c=a+b
    return c

def restar(a, b):
    return a -b

def multiplicar(a, b):
    return a*b

def div_entera(a, b):
    if b==o:
        print("error división sobre cero")
        return
    return a//b

def div_entera(a, b):
    if b==o:
        print("error división sobre cero")
        return
    return a/b

def modulo(a,b): #regresa residuo
    if b == 0:
        print("error división sobre cero")
        return
    return a%b

def potencia(a,b):
    return a**b

def main():
    print("ingresa dos valores")
    x = int(input())
    y = int(input())
    print("1.sumar\n2.restar\n3.división entera")
    print("4.división\n5.módulo\n6.potencia\n7.multiplicar\n8.Salir")
    op = int(input())
    if op == 1:
        print(sumar(x, y))
    elif op == 2:
        print(restar(x, y))
    elif op == 3:
        print(div_entera(x, y))
    elif op == 4:
        print(división(x, y))
    elif op == 5:
        print(modulo(x, y))
    elif op == 6:
        print(potencia(x, y))
    elif op == 7:
        print(multiplicar(x, y))
    elif op >= 8:
        print("Hasta luego")

if __name__ == "__main__": #Validamos la función
    main()
