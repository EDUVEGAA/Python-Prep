## Flujos de Control


for n in range(1,10):
    print(n)
    
    
##############
#lo podes dejar así o también escribir: 
    print(f"{i}  elevado al cubo es:  {i**3}")
    ###############################################333

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

#import app #importa el archivo app.py
#from numpy import apply_along_axis


#def saludo_func2():
        #print('HOLA #1')
#if __name__ == '__main__':
        #saludo_func2()

def ingresar_func1():
    
        a = int(input('Ingrese un numero: '))
#a = 10
        if (a < 0):
            print('La variable es menor a cero')
        elif (a > 0): 
            print('La varaible es mayor a cero')
        else:
            print('La variable es igual a cero')
if __name__ == '__main__':
    ingresar_func1()
    saludo_func2() #importa el archivo app.py
    ###########################################
a = 2
b = 3
if (type(a) == type(b)):
    print('Las variables son del mismo tipo de dato')
    print(f'Las variables {a} y {b} son del mismo tipo de dato')
    print(f'Las variables' , str(a), 'y', str(b), 'son del mismo tipo de dato')
    print(f'Las variables ' + str(a) + ' y ' + str(b) + ' son del mismo tipo de dato')
    
    #############
2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

def comparar_func3():
    a = str(input('Ingrese a: '))

    b = int(input('Ingrese numero b: '))

    if (type(a) == type(b)):
        print('Las variables son del mismo tipo de dato')
    else:
        print('Las variables son de tipos de dato diferentes')
comparar_func3()

3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

for i in range(1, 21):
    if i % 2 == 0:
        print('El número ', str(i), ' es par')
    else:
        print('El número ', str(i), ' es impar')
        
##############################3
def ingresar_func4():
        #num = int(input('Ingrese un numero: '))
        n=0
        while n < 20: #mientras n sea menor a 3
             n+=1
            
             if n % 2 == 0:
                print('El número ', str(n), ' es par')
             else:
                print('El número ', str(n), ' es impar')
            
ingresar_func4()
    
############
###ejemplo
def piezas_func():  
    cantidad=0
    x=1
    n=int(input("Cuantas piezas cargara:"))
    while x<=n:
        largo=float(input("Ingrese la medida de la pieza:"))
        if largo>=1.2 and largo<=1.3:
            cantidad=cantidad+1
        x=x+1
        print("La cantidad de piezas aptas son")
        print(cantidad)        
piezas_func()
  


4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

for i in range(0, 6):
        print('Valor es', str(i), ' Elevado a la potencia es', str(i**3))
        n=i**3
        if n % 2 == 0:
            print('El número ', str(n), ' es par')
        else:
            print('El número ', str(n), ' es impar')



5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
def ingresar_func4():
    n = int(input('Ingrese un numero: '))
    #n = 12
    for i in range(0, n):
        pass
    print(i)
ingresar_func4()

6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

def factor_func5():
    n = str(input("Ingrese un numero: "))
    z = int(n)
    if (type(n) == int):
            if (z > 0):
                factorial = z
                while (z > 2):
                     z = z - 1
                     factorial = factorial * z
                     
                print("El factorial de ",   str(n) , "es ", factorial)
            else:
                print("La variable ", z , " no es mayor a cero")
    else:
        print("La variable no es un entero")
factor_func5()



def factor_func7():
        n = input("Ingrese un numero: ")
    #n = -4
        if (type(n) == int):
            if (n > 0):
                factorial = n
                while (n > 2):
                     n = n - 1
                     factorial = factorial * n
                print('El factorial es', factorial)
            else:
                print('La variable no es mayor a cero')
        else:
            print('La variable no es un entero')
factor_func7()

def factor_func6():
    n = input("Ingrese un numero: ")
    #n = 4.1
    if (type(n) == int):
        if (n > 0):
            factorial = n
            while (n > 2):
                n = n - 1
                factorial = factorial * n
            print('El factorial es', factorial)
        else:
            print('La variable no es mayor a cero')
    else:
        print('La variable no es un entero')
factor_func6()


n = int(input("Ingrese un numero: "))
#n = float(z)
if (type(n) == float):
    if (type(n) == int):
        if (n > 0):
            factorial = n
            while (n > 2):
                n = n - 1
                factorial = factorial * n
            print('El factorial es', factorial)
        else:
            print('La variable no es mayor a cero')
else:
    print('La variable no es un entero')
####################3
#entrada INPUTS de datos ATS 

def num_func7():
        n = int(input("Digite un numero: "))  
        print(f"El numero es {n+1}")
    
num_func7()


#Funciones sin rotorno de valor 

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Flor")
saludar("Carlos")


#######################################3


def hazLevel():
        depth= float(input("INGRESE depth:"))
        speed= float(input("INGRESE speed:"))
        if depth < 1.4:
           return 1
        elif (depth < 2.5 and speed < 2.5):
           return 2
        else:
           return 3
hazLevel()

7) Crear un ciclo for dentro de un ciclo while
n = 0
while(n < 5):
    n += 1
    for i in range(1,n):
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))

8) Crear un ciclo while dentro de un ciclo for


def new_func(n):
    n = 5
    for i in range(1, n):
            
            while(n < 5):
                n -= 1
            print('Ciclo while nro ' + str(n))
            print('Ciclo for nro ' + str(i))

#new_func(n)
-------------
Ciclo while nro 5
Ciclo for nro 1
Ciclo while nro 5
Ciclo for nro 2
Ciclo while nro 5
Ciclo for nro 3
Ciclo while nro 5
#Ciclo for nro 4

TABLA MULTIPLICAR DEL N:
    
def multi_func8():
    n = int(input("Digite un numero: ")) 

    for i in range(1, 13):
        print('Tabla '+ str(i) + ' X '+ str(n) +" = "+ str(i*n))
multi_func8()


9) Imprimir los números primos existentes entre 0 y 30



10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6