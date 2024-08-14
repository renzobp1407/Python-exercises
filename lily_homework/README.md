resolucion del ejercicio:

# Entendimiento

la tarea de lily es un ejercicio que consiste en un array de elementos `n` cuyo elementos deben ordenarse de tal forma que se considere un arreglo bonito `an Array is Beautiful` el cual cosiste en estar organizado de menor a mayor, este array se debe lograr moviendo 2 elementos de la lista hasta que esté organizado de menor a mayor y en el menor numero de movimientos posible

# Resolución

- el ejercicio trate de abordarlo de diferentes enfoques debido a que no es fácil buscar la forma mas optima de acomodar un array, es por eso que dividí el problema en varias partes:



- primeramente hice una sección para hallar la cantidad de cambios que se deben realizar en un array dado, esta sección luego la convertí en una función llamada `total_list_swaps`, la cree en una funcion aparte porque en mitad del codigo tenia duplicados y unirlo en una sola parte lo podia entender mejor

- entendí que si yo ordeno el array de mayor a menor e intento iterar, el arrojará un resultado, pero si lo organizo de menor a mayor esté arrojará otro resultado, haciendo que se tenga que comparar cual de los 2 fue el que menos pasos tuvo para organizar el array, en base a esto partí para realizar el ejercicio

- declaro 2 variables: `number_of_swaps` que contendrá el numero de cambios que se realizaron y `position_list_values` que tendrá el rastreo de las posiciones

- declaro un for para recorrer toda la lista de `arr` 

- hago un if preguntando si el elemento actual no está donde deberia estar, entonces suma un +1 a `number_of_swaps`

- En la variable `swap_index` voy agregando los elementos que deberian estar en la posición i

- ahora actualizamos la variable `position_list_values` con la nueva posición del elemento que se está moviendo

- por ultimo intercambiamos los elementos en el array de `arr`, intercambiamos `arr[i]` con `arr[swap_index]`

- retornamos en la minifuncion `number_of_swaps` con el numero total de cambios realizados en el array

- al tener esta funcion lista, puedo ahora pasarle como parametro el array original y una versión organizada del array de mayor a menor o de menor a mayor

- creo 2 variables: `ascended_swaps` con el parametro del array organizado de mayor a menor junto al original y `descended_swaps` que se le pasa el parametro array organizado de menor a mayor junto al original

 previamente a eso, creo 2 variables que serán los array organizados ascendente `sorted_array` y otro descendente o reversa `sorted_array_reverse`

- por ultimo, utilizo el return junto a un funcion de `min` para saber cual de las 2 variables `ascended_swaps` o `descended_swaps` fue la que tuvo un numero menor de cambios