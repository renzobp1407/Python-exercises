resolucion del ejercicio:

# Entendimiento

un florista quiere vender sus flores a un numero de clientes, para esto el va a vender la primera flor a su prpecio original, pero la segunda va a ser el doble del costo, la tercera al triple de precio y así, se debe hallar el costo minimo de comprar todas las flores del florista

# Resolución

- para este ejercicio me dan el numero de amigos con `k` y `c` el valor de cada flor

- declare 1 variable llamada `total_cost`. y `c` lo organicé de mayor a menor gracias al `sort` y `reverse`

- empezé un for que recorrerá toda la lista `c` 

- apliqué la formula descrita para hallar el valor minimo: `total_cost` se va sumar con la división entera de `(i // k) + 1` para hallar el valor normal o doble del costo y se multiplicará por el valor actual de la flor `c[i]`

- hago un print para ir comprobando el valor de la iteración, porque la formula anterior tuve que ir haciendole ajustes

- hago un return de la variable `total_cost`

