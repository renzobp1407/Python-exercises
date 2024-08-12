resolucion del ejercicio:

# Entendimiento
a traves de 2 valores que son el numero de juegos y un array con el valor de las anotaciones, se debe encontrar el numero de veces que se rompe el record de anotacion mas alto y anotaciones más bajo

se deberá devolver un array de 2 valores, el primero con las anotaciones mas altas y el segundo con las anotacion mas baja

# Resolución

- para poder resolver el ejercicio, primero declare un For que recorriera el array de todas las anotaciones de `score`

- luego de plantearlo, saqué que variables necesitaba para el for: ``high_score`` para la puntuación alta, ``low_score`` para la puntuación baja, ``break_high_record`` para contar las veces de cuando se rompia un nuevo record de alta puntuación, ``break_low_record`` para contar las veces de cuando se rompia un record de baja puntuación y ``record_break`` como variable para retornar el record.

  las variables ``high_score`` y ``low_score`` le asigné el valor de la primera anotación para que se pudiera comprar en el siguiente if dentro del for

- dentro del for, agregué 2 condiciones if, el primero que preguntara si el valor de la primera anotación es mayor que el ultimo valor de la puntuación alta, este entra y: asignaba ``high_score`` con la posicion actual de anotaciones `scores[i]`, sumaba una anotacion en la variable de``break_high_record`` y asigna `record_break[0]` con el valor de las veces que se ha roto el record `break_high_record`

  el segundo if preguntara si el valor de la primera anotación es menor que el ultimo valor de la puntuación baja, este entra y: asignaba ``low_score`` con la posicion actual de anotaciones `scores[i]`, sumaba una anotacion en la variable de``break_low_record`` y asigna `record_break[1]` con el valor de las veces que se ha roto el record `break_low_record`

- al ver que habia un caso que puede que todos los valores de los juegos pueden ser iguales, los valores de ``high_score`` y ``low_score`` se mantenian iguales y no arrojaba 0, entonces cree 2 condicionales if mas

 el primero pregunta si el valor de ``low_score`` es igual al primer valor de las anotaciones `scores[0]` y que i sea igual al ultimo valor de la longitud del for, entonces los asignaba con valor 0

 el segundo pregunta si el valor de ``high_score`` es igual al primer valor de las anotaciones `scores[0]` y que i sea igual al ultimo valor de la longitud del for, entonces los asignaba con valor 0

- y por ultimo realizo el return de la funcion
