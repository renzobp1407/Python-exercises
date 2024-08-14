resolucion del ejercicio:

# Entendimiento

el ejercicio explica que hay un rankeo de jugadores con puntajes y un jugador inividual en donde se comparan para saber el la posición del jugador con respecto a los otros jugadores, el objetivo es hallar la posición de cada juego del jugador individual

# Resolución

- para plantear el ejercicio, primero organicé una nueva lista llamada `scores` para obtener los puntajes de forma organizada, eliminando los duplicados y de mayor a menor

- declare 2 variables mas que son `result[]` que es una lista e `index` que es el largo de la lista de `scores`

- declaré un for para que recorriera la lista de los puntajes de `player`

- dentro del for, declaré un while que le indico que el `index` sea mayor o igual a 0 y que `p`  que es la puntuación sea mayor o igual a la puntuación (de los otros jugadores) en la posición actual, esto es con el objetivo de reducir el `index` en uno para moverse al siguiente valor mas bajo y así sumarte +2 al indice y hallar el valor de la posición del jugador

- por ultimo, realizo el return de `result` con la lista 