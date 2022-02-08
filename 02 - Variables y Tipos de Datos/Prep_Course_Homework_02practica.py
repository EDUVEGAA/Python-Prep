## Variables

1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
import random
x = random.randint(0,10000000)
print(x)
     
2) Imprimir el tipo de dato de la constante 8.5
#import types
x = 8.5
print(type(x))

x = 69
print(type(x))

3) Imprimir el tipo de dato de la variable creada en el punto 1
import random
x = random.randint(0,10000000)
print(type(x))

4) Crear una variable que contenga tu nombre
nombre = 'eduardo'
print(nombre)

5) Crear una variable que contenga un número complejo
x = 3 + 2j
print(x)

6) Mostrar el tipo de dato de la variable crada en el punto 5
x = 3 + 2j
type(x)
7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
Pi=3.1415926535897932
print(round(Pi,4))

8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var1 = 'True'
var2 = True

9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
var1 = 'True'
var2 = True
print('La variable 1 es de tipo:', type(var1))
print('La variable 2 es de tipo:', type(var2))

10) Asignar a una variable, la suma de un número entero y otro decimal
x = 8 + 4.6
print(x)

11) Realizar una operación de suma de números complejos
a = 3 + 4j
b = 2 + 1j
print(a + b)

12) Realizar una operación de suma de un número real y otro complejo
c = a + 1.61
print(c)

13) Realizar una operación de multiplicación
x = 8 * 4.6
print(x)
14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)
15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
print(27 / 4)
16) De la división anterior solamente mostrar la parte entera
print(27 // 4)
17) De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)
18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*(27 // 4)+(27 % 4))
19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var1 = '3duard0 '
var2 = 'v3g4'
print(var1 + var2)

20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a = "2"
b = 2
def new_func():
    print 'falso porque "2" es texto'

if b == a:
    print "verdad porque son valores numericos"
else:
    new_func()
  
21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
a = int('2')
b = 2
def new_func():
    print 'falso porque "2" es texto'

if a == b:
    print "verdad porque son valores numericos"
else:
    new_func()

22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a = float('3,8')
porque es texto

23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
a = 3
a -= 1
print(a)
#x-=1 es equivalente a x=x-1
24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

a=1
print(a<<2)
# 4

bin(4)
#'0b100'
#bits se desplazan a la derecha según el número de bits estipulado por el segundo operando. 
#Los bits iniciales hacia la izquierda como resultado del desplazamiento se establecen en 0.
25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

2 + '2'
error porque los dos operandos no son del mismo tipo

float(2) + float('2')
#4.0

int(2) + int('2')
#4

str(2) + str('2')
#22

26) Realizar una operación válida entre valores de tipo entero y string

var1 = 'texto '
var2 = 3
print(var1 * var2 + 'se repite ' + str(var2) + ' veces')