resolucion del ejercicio:

# Entendimiento

Hallar el factorial de un numero ingresado


# Resolución

- declaré una variable `new_factorial` para tener el nuevo numero factorial

- inicié un for con un rango de 1 hasta n+1, es decir desde el 1 hasta el numero ingresado n

- dentro de la condicion, creo un if que diga si `i == n` entonces rompa el ciclo for

- el siguiente if es si `i == 1` haga la multiplicación de n que es el valor actual contra n-i que seria el siguiente numero 

- sino, en vez de n seria `new_factorial` por n-1 que seria el siguiente valor

- por ultimo realicé el resturn de la función `new_factorial`

---

## Update: 

ese ejercicio no cumplia con todos los test cases, por el cual decidí cambiar el enfoque de la condicion interior del for, ahí es donde cree el otro archivo `extra_long_factorial_2.py`

- en este nuevo codigo, `new_factorial` lo declaré en 1

- en la condicion del for puse `n - 1` para que no se pasara del indicie

- el valor de `new_factorial` va a ser `(new_factorial * (n - i))` para ir multiplicando el valor actual con el siguiente de la lista

- por ultimo realicé el resturn de la función `new_factorial`