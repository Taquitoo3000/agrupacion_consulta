# Agrupacion de Consulta
Este código toma un data frame y lo agrupa por ID, en este caso llamado "Expediente". Tiene distintos campos.
Cada campo llama a una función de concatenacion según las necesidades del dataframe.

## Función concatenar_valores_unicos
Esta funcion usa
``
.dropna().unique()
``
para quitar los valores nulos y tomar solo los valores unicos sin repetir, despues condicionalmente retorna nada si no hay nada en el campo, retorna la primer cadena si solo es una y retorna las distintas cadenas separadas por comas si hay mas de una

## Función concatenar_valores
Esta función hace lo mismo que la anterior pero sin
``
.unique()
``
para poder repetir los campos que encuentre y separarlos por comas a pesar de que se repitan
