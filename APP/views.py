from django.shortcuts import render
from APP.models import Familiares
from django.http import HttpResponse

def familia(request):
    familiar1= Familiares("Jesica","34",  "19/04/88")
    familiar2= Familiares("Mateo", "1", "14/06/21")
    familiar3= Familiares("Luis", "35",  "23/10/86")

    diccionario= {"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3}
    return render (request, "template.html", diccionario)
    
 


# Create your views here.
