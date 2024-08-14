resolucion del ejercicio:

# Entendimiento

el programa entregaba una hora y minuto como valores, estos valores deben comvertirse a letras para poder dar la hora exacta con sus diferentes combinaciones como lo sugiere el programa y así entregar la hora correcta

# Resolución

- al principio validé todo lo que son las diferentes tipos de combinaciones para poder dar la hora, es decir, cuando es 0, 1, 15, 30, 45, entre 1 y 15, entre 15 y 30, entre 30 y 45, entre 45 y 60

- al entender las combinaciones, intenté al principio dar el resultado directamnte  con palabras pero tuve problemas con las palabras al ser muchas

- entonces decidí crear 2 listas, una con las letras de las horas y los minutos (y le agregué un espacio al primer caracter para representar el 0)

- a estas listas cuando se necesitara dar la hora o los minutos, solamente le pasaba al array la posición h `hours_to_letters[h]` o m `minutes_to_letters[m]` para que escogiera su equivalente en letras 

- agregué una variable llamada `complete_time_word` para registrar el string despues de entrar a la condicion

- al tener claro eso, decidí agregar las condiciones if en un orden especifico para asegurar que los minutos si coincidan con las condiciones:
  
  el orden seria cuando m tenga el valor: de 0, 1, 15, 30, 45, entre 1 y 15 o 15 y 30, entre 30 y 45 o 45 ay 60

- cuando empecé a agregar las letras, tuve en cuenta los espacios que estos generaban antes o despues de dar los numeros en horas o minutos

- en la ultima condicion de los minutos, para que me diera los minutos faltantes para la siguiente hora dentro de la posición restaba 60-M `minutes_to_letters[60 - m]` y para la siguiente hora le agregaba un +1 a h  `hours_to_letters[h+1]`

- por ultimo hice el return de la variable `complete_time_word`

- tuve problemas en algunos test cases pero por temas de espacios en las palabras de `quarter past` que ajuste agregando el respectivo espacio al final del string