from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def barra(request):
    respuesta = "Esto es la barra,"
    respuesta += " y esto es lo que hay:"
    lista = Pages.objects.all()
    for pagina in lista:
        respuesta += '<br><a href="/page/' + str(pagina.id) + '">' + pagina.name + '</a>'

    return HttpResponse(respuesta)

@csrf_exempt
def pagina(request,identificador):
    if request.method == "GET":     #Si hacemos un GET es que estamos pidiendo ..../pagina/id
        try:
            pagina = Pages.objects.get(id=identificador)
            respuesta = "Has introducido " + pagina.name + " que corresponde a: " + str(pagina.page) + " y el id es: " + str(pagina.id)
        except Pages.DoesNotExist:
            respuesta = "No existe la pagina con el identificador " + str(identificador) + ". Creala tu "
            respuesta += '<form action="" method="POST">'
            respuesta += 'Nombre: <input type="text" name="nombre">'
            respuesta += '<br>Pagina: <input type="text" name="pagina">'
            respuesta += '<input type="submit" value="Enviar"></form>'

    elif request.method == "PUT":       #Si hacemos un PUT es que estamos haciendo un envio de formulario pero puede qque la pagina ya estuviese
        try:
            pagina = Pages.objects.get(id=identificador)
            respuesta = "Ya existe una pagina con identificador: " + str(identificador)
        except Pages.DoesNotExist:
            body = request.body.split(',')
            pagina = Pages(name=body[0], page=body[1])
            pagina.save()
            respuesta = "Se ha guardado la pagina: " + name \
                        + ", con identificador " + str(pagina.id)

    elif request.method == "POST":      #Si hacemos POST estamos añadiendo una nueva pagina a la lista mediante el formulario
        nombre = request.POST['nombre']
        pagina = request.POST['pagina']
        pagina = Pages(name=nombre, page=pagina)
        pagina.save()
        respuesta = "Se ha guardado la pagina: " + nombre \
                    + ", con identificador " + str(pagina.id)

    else :
        respuesta = "Metodo no permitido"


    return HttpResponse(respuesta)
