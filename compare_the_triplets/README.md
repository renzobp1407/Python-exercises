resolucion del ejercicio:

# Entendimiento

Alice y Bob crearon unos ejercicios para hackerrank, esos ejercicios se miden por 3 parametros que son claridad, originalidad y dificultad. hay que comparar ambos ejercicios de ellos con cada parametro calificado, por cada valor mayor del parametro, se le agrega un punto, el que tenga mas puntuación despues de comrparar los parametros entre los 2, gana el juego


# Resolución

- las puntuaciones de Alice y Bob estan representadas en 2 listas, lo cual lo resprentadas en `a` y `b`

- declaré una variable `results` que es una lista que tendrá la sumatoria de puntos de Alice en `results[0]` y bob en `results[1]`

- cree un for para que recorriera toda la lista (cualquier array de `a` y `b` funciona)

- dentro del for, agregué 2 condicionales if: 

  si `a[i]` es mayor a `b[i]`, entonces agregaba un +1 a `results[0]` que representa a Alice

  si `a[i]` es menor a `b[i]`, entonces agregaba un +1 a `results[1]` que representa a bob

- por ultimo escribí el return de la variable `results`