resolucion del ejercicio:

# Entendimiento
validar cual de los 2 gatos estaba mas cerca del ratón e imprimirlo en pantalla, si ambos esaban a la misma distancia, se imprimia al raton

# Resolución

- Declare 2 variables "cat_a_distance_to_mouse" para  obtener la distancia del Gato A al ratón y "cat_b_distance_to_mouse" para obtener la distancia del Gato B al ratón

- en estas variables realicé una resta entre el numero del ratón menos el Gato A y ratón menos el Gato B para hallar la distancia

- debido a que existia la posibilidad que una de las variables me diera un numero negativo, utilicé la función abs() que conviernte un numero a su forma absoluta sin negativo

- Realicé un primer if que validara que si el gato A estaba a la misma distancia que el gato B (tuvieran el mismo valor) imprimiria que ganó el ratón asignandole a la variable "cat_mouse_string" la cadena "Mouse C" 

- continuando al if, realicé un elif pero ahora comparando el valor del Gato A es menor que el Gato B, entonces le asigno la variable "cat_mouse_string" la cadena "Cat A" 

- utilicé de nuevo un ultimo elif para comparar que el valor del Gato B es menor que el Gato A, entonces le asigno la variable "cat_mouse_string" la cadena "Cat B"

- por ultimop realizo un return de la variable "cat_mouse_string" para la impresión del string







