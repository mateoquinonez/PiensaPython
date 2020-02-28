''' Existen varios tipos de operaciones en Python.

El primero, y mas comun es el de la adicion.

'''

x, y, z = 3, 9, '4'
a = 'String'
b = [1, 2, 'lol']


'''
La siguiente linea de codigo imprimira el resultado de sumar x con yield
'''

print(x+y)

''' 

Aqui print() es una funcion. Una funcion es un pedazo de codigo
que generalmente toma algunos datos de entrada, lo procesa y te responde con una salida. Esta salida
se llama valor de retorno (return value).
'''
'''
Debemos recordar que es imposible en la gran mayoria de los casos, sumar variables 
de diferentes tipos. En ese caso, poner 

print(x+z)

nos daria un error, puesto que z es del tipo string.



Sin embargo, es posible sumar dos listas
'''

c = [False, '123', 42]

print(b + c)

#la ultima linea seria parecido a b.extend(c)
#sin embargo, b.extend(c) es en realidad b = b + c. Asignandolo a b.

# Tambien podemos sumar strings, esto va a resultar en lo que se llama concatenacion

print(a + a)

''' 
En general, la suma es de las pocas operaciones compartidas por distintos tipos.
El resto de operaciones, que listaremos a seguir son usadas mayoritariamente para
el tipo numerico

Resta (-):

6 - 5

Multiplicacion (*):

12 * 4

Division (/):

4 / 2 

Potenciacion ( ^ ) :

3 ^ 4  (o, equivalentemente, pow(3, 4), o 3 ** 4 )

Resto de division ( % ) :

12 % 7 El resto de la division de 12 entre 7. En este caso es 5

'''
#OPERADORES RELACIONALES

'''
 Existen operadores que comparan valores
 > (es mayor a)
 < (es menor a)
 == (es igual a)
 != (no es igual a)
 >= (es mayor que o igual a)
 <= (es menor que o igual a)
'''
#operador "es mayor a"

num1 = 7
num2 = 13
num1 > num2

#operador "es menor a"

num1 < num2

#operador "es igual a"

num1 == num2

#operador "no es igual a"

num1 != num2

#OPERACIONES LOGICAS

'''
 En ciertas ocaciones, necesitamos exponer a nuestro programa a ciertas
 condiciones. Consideremos el siguiente ejemplo:
 
 Python, comprame una empanada si hay plata y si la despensa tiene 
 empanada de pollo.

¿Como le decimos a python que haga la instruccion?
Usando el operador and ( & )

'''

hay_plata = False
hay_empanada = True

comprar = hay_empanada and hay_plata #equivalentemente, hay_empanada & hay_plata

'''
El operador and recibe DOS booleans, y devuelve UNO. Este resultado sera verdadero
solamente si los dos booleans, sean verdadero, caso contrario devolvera Falso.

Otro operador muy comun es el operador booleano or ( | )

'''

print(hay_empanada or hay_plata) #equivalentemente, hay_empanada | hay_plata

'''
Un ultimo operador, es la negacion. Se pone al inicio del boolean, y lo cambia de sentido

'''

no_hay_plata = not hay_plata #sera Verdadero

'''
Recuerden que al igual que en matematicas, Python va a realizar lo que este dentro
de parentesis en primer lugar.

'''

print (not ( False and (True or True) ) )

#que va a imprimir la consola?

#OPERACIONES DE PERTENENCIA

'''
 Este tipo de operadores nos ayudan a verificar si cierto valor esta en otro 
 in (esta en)
 not in (no esta en)
'''

2 in [1, 2, 3]

'libro' in 'mochila'

2 not in (1, 2, 3)

'libro' not in 'mochila'

#OPERADORES DE IDENTIDAD

'''
 Los operadores de identidad verifican si dos variables son identicas.
 is (es)
 is not (no es)
'''

2 is 2.0

a = 8
b = a
a is b

c = 8
a is c

0 is not False
