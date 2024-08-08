resolucion del ejercicio:

# Entendimiento
en un Array binario de "0" y "1" se deberá evitarlas nubes que se encuentren con el valor de "1", para eso se realizan saltos en el index de 1 a 2 espacios para solo estar en posiciones donde se encuentre "0"

# Resolución

- para poder solucionar los saltos en la lista, tuve que crear cada escenario posible en los inputs que estos me daban al inicio que son "0 0 1 0 0 1 0 " que es impar y "0 1 0 0 1 0" que es par

- cree un for para que recorriera toda la lista

- primer escenario planteado fue si el valor inicial es "0" y le sigue un "1" entonces este iba a realizar un salto, le asignaba a la variable "sum_jumps" un +1 y al index "i" un +2 para que este avanzara en el recorrido

- segundo escenario anidado por "elif" cuando el valor inicial donde se encuentra es "0", el que sigue es "1" y el tercero adelante es "0", al hacer esto le asignaba a la variable "sum_jumps" un +1 y al index "i" un +2 para que este avanzara en el recorrido y no quedara en un "1" en la lista

- tercer escenario anidado por el "elif", cuando el valor inicial donde se encuentra es "0", el que sigue es "0" y el tercero adelante es "1", al hacer esto le asignaba a la variable "sum_jumps" un +1 y al index "i" un +1 para que este avanzara en el recorrido no quedara en un "1" en la lista

- cuarto escenario anidado por el "elif", cuando el valor inicial donde se encuentra es "0", el que sigue es "0" y el tercero adelante es "0", al hacer esto le asignaba a la variable "sum_jumps" un +1 y al index "i" un +2 para que este avanzara en el recorrido no quedara en un "1" en la lista

- al ver esto, realizaba el escenario del impar sin problemas, pero al ver que el par se salia de la lista y arrojaba un error agregué un escenario extra para cuando esté en el final del recorrido

  si el indice "i" era igual al ultimo en la lista "len(c)-1" este iba a comparar con otro if anidado preguntado si el valor inicial es "0" y le sigue un "1" entonces este iba a realizar un salto, le asignaba a la variable "sum_jumps" un +1 y al index "i" un +1 y generaba un "Break" para que este detuviera la iteracion "for"

  esta condicion la ubique en el primer if de la cadena de "elif" porque el escenario es para cuando este al final del recorrido de la lista y no afecte los demas "elif"

- y para que en el caso del impar no sacara error, hice otra condicion al principio del for en el que si el indice sumado con "+2" era mayor o igual al largo de la lista "len(c)" este realiza un "Break" para detener el ciclo "for"

- por ultimo realizé el "return" de la variable "sum_jumps" con el valor del total de saltos realizados

### update:

al ejecutar el **jumping_clouds.py** no resolvia todos los casos de uso, es por eso que decidí empezar a resolverlo de nuevo


---	

### update: 7/8/2024

Empecé a realizar el ejercicio y quedó guardado en **jumping_clouds2.py**

- al ver que los test cases me fallaban, decidí darle mejor un enfoque con 'while' por que sentia que podia controlar mejor las iteraciones del array

- decidí empezar con 3 'if' que validaban 3 posiciones para contar los saltos (inicial, siguiente +1 y siguiente +2 ) y sumar al indice +1 para que avance en el array

- realicé un print a la variable 'sum_jumps' para verificar su valor y llevar el seguimiento de los saltos

- al seguir la ejecución del array, me daba cuenta que no validaba el caso que 'i+2' se quedaba sin indice pero 'i+1' si tenia indice, entonces me arrojaba error y decidí hacer las 2 siguietes condiciones:

```python
if(i+2 > len(c) - 1 ):
    break
if(i+1 > len(c) - 1):
    break    
```

al hacerlas con los impares no tenia problemas, pero con los pares que el indice 'i+1' sobraba, no sumaba ese ultimo (o 2 ultimos)

- entonces decidí realizar mas validaciones de la siguiente manera:

```python
if(i+2 > len(c) - 1 ):
    if(i+1 == len(c) - 1):
        if (c[i] == 0 and c[i+1] == 0):
            sum_jumps += 1
            i += 1            
        elif (c[i] == 0 and c[i+1] == 1):
            break
        
if(i+1 > len(c) - 1):
    break
```

de esta forma, aseguraba que se validaran los indices finales sin que se salieran del loop for

