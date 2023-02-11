#Importamos template
from django import template
#definimos el decorador register a partir de Library
register = template.Library()

#Aplicamos el decorador register
@register.filter
#definimos la función índice que nos permite desplegar el valor de un índice en el template.
#Recibe como parámetro un indexable y el índice i.
def index(indexable, i):
    #Devolvemos el valor del índice i del indexable.
    return indexable[i]
