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
from django.contrib.auth       import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"facil/home.html")

# @login_required
def articulos(request):
    contexto = {'articulos': Articulo.objects.all()}
    return render(request,"facil/articulos.html", contexto)

# @login_required
def articulo(request):
    # enviar no Articulo.objects.all() sino el id específico del artículo que seleccionó el usuario
    contexto = {'articulo': Articulo.objects.all()}
    return render(request,"facil/articulo.html", contexto)

@login_required
def comentarios(request):
    return render(request,"facil/comentarios.html")

@login_required
def acerca(request):
    return render(request,"facil/acerca.html")

@login_required
def contacto(request):
    return render(request,"facil/contacto.html")

@login_required
def perfil(request):
    return render(request,"facil/perfil.html")

@login_required
def buscar(request):
    return render(request, "facil/buscar.html")

@login_required
def usuarios(request):
    return render(request, "facil/usuarios.html")




# AGREGAR FUNCIÓN PARA RENDERIZAR LAS ESPECIFICACIONES DE UN ARTICULO
def verArticulo(request):
  pass

#------------------------------Forms-------------------------------------------------------------------------

#---------------------Acciones---------------------------------------------

#----------------------------Crea--------------------------------------------
@login_required
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
@login_required
def buscarArticulos(request):
    patron = request.GET.get("buscar", None)
    if patron:
        articulos = Articulo.objects.filter(nombreArt__icontains=patron)
        contexto = {"articulos": articulos}
        return render(request, "facil/articulos.html", contexto)
    return HttpResponse("No se ingresaron patrones de búsqueda")

#---------------------------------------------Edita o Actualiza------------------------------------------------------------
@login_required
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
@login_required
def deleteArticulos(request, id_articulo):
    articulos= Articulo.objects.get(id=id_articulo)
    articulos.delete()
    return redirect(reverse_lazy('articulos'))


#----------------------------------------Usuarios---------------------------------------------------------------

class UsuarioList(LoginRequiredMixin, ListView):
    # La siguiente línea es la que agregamos 
    login_url = reverse_lazy('login')
    model= Usuario

    class login_required_mixin_admin(LoginRequiredMixin):
        model= reverse_lazy('login')

class UsuarioCreate(LoginRequiredMixin, CreateView):
    model= Usuario
    fields= ['nombre','apellido','email']   #Los campos que quiero que me muestre en el formulario, son exactamente los que están en el models.
    success_url= reverse_lazy('usuarios')

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model= Usuario
    fields= ['nombre','apellido','email']  
    success_url= reverse_lazy('usuarios')

class UsuarioDelete(LoginRequiredMixin, DeleteView):
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
            return redirect(reverse_lazy('home'))
    
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

def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))

#----------------------------------------------Editar perfil--------------------------------------

@login_required
def editarperfil(request):
    usuario= request.user

    if request.method == "POST":
        miform= RegistroForm(request.POST)
        if miform.is_valid():
            usuario = miform.cleaned_data.get("username")
            miform.save()
            return redirect(reverse_lazy('home'))
        
    else:
        miform= RegistroForm()
    
    return render(request, "facil/registro.html", {"form":miform})


