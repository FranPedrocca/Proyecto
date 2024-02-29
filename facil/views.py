from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login


# Create your views here.
def home(request):
    return render(request,"facil/home.html")

def articulos(request):
    contexto = {'articulos': Articulo.objects.all()}
    return render(request,"facil/articulos.html", contexto)

def comentarios(request):
    return render(request,"facil/comentarios.html")

def acerca(request):
    return render(request,"facil/acerca.html")

def contacto(request):
    return render(request,"facil/contacto.html")

def buscar(request):
    return render(request, "facil/buscar.html")

def usuarios(request):
    return render(request, "facil/usuarios.html")





#------------------------------Forms-------------------------------------------------------------------------

#---------------------Acciones---------------------------------------------

#----------------------------Crea--------------------------------------------

def createArticulo(request):
    
    if request.method == "POST":
        miform= ArticuloForm(request.POST)
        if miform.is_valid():
            
            articulo_nombre = miform.cleaned_data.get("nombre")
            articulo_modelo = miform.cleaned_data.get("modelo")
            articulo= Articulo(nombreArt= articulo_nombre, modeloArt= articulo_modelo)
            articulo.save()
            return redirect(reverse_lazy('articulos'))
    else:
        miform= ArticuloForm()
    return render(request, "facil/articulosForm.html", {"form":miform})

#-------------------------------Busca-----------------------------------------------

def buscarArticulos(request):
    patron = request.GET.get("buscar", None)
    if patron:
        articulos = Articulo.objects.filter(nombreArt__icontains=patron)
        contexto = {"articulos": articulos}
        return render(request, "facil/articulos.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")

#---------------------------------------------Edita o Actualiza------------------------------------------------------------

def updateArticulos(request, id_articulo):
    articulo= Articulo.objects.get(id= id_articulo)
    if request.method== "POST":
        miform= ArticuloForm(request.POST)
        if miform.is_valid():
            articulo.nombreArt = miform.cleaned_data.get('nombre')
            articulo.modeloArt = miform.cleaned_data.get('modelo')
            articulo.save()
            return redirect(reverse_lazy('articulos'))
    else:
        miform= ArticuloForm(initial={
            'nombre':articulo.nombreArt,
            'modelo':articulo.modeloArt})
    return render(request, "facil/articulosForm.html", {"form":miform})

#-------------------------------------------Elimina---------------------------------------------------------------

def deleteArticulos(request, id_articulo):
    articulos= Articulo.objects.get(id=id_articulo)
    articulos.delete()
    return redirect(reverse_lazy('articulos'))


#----------------------------------------Usuarios---------------------------------------------------------------




class UsuarioList(ListView):
    model= Usuario

class UsuarioCreate(CreateView):
    model= Usuario
    fields= ['nombre','apellido','email']   #Los campos que quiero que me muestre en el formulario, son exactamente los que están en el models.
    success_url= reverse_lazy('usuarios')

class UsuarioUpdate(UpdateView):
    model= Usuario
    fields= ['nombre','apellido','email']  
    success_url= reverse_lazy('usuarios')

class UsuarioDelete(DeleteView):
    model= Usuario
    success_url= reverse_lazy('usuarios')


#---------------------------------Login, Logout, Registrarse,-------------------------------------------------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return render(request, "facil/home.html")
        else:
            return redirect(reverse_lazy('login'))
    
    miform= AuthenticationForm()
    
    return render(request, "facil/login.html", {"form":miform})



def register(request):
    if request.method == "POST":
        miform= RegistroForm(request.POST)
        if miform.is_valid():
            usuario = miform.cleaned_data.get("username")
            miform.save()
            return redirect(reverse_lazy('home'))
        
    else:
        miform= RegistroForm()
    
    return render(request, "facil/registro.html", {"form":miform})