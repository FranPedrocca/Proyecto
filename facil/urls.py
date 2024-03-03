from django.urls import path, include
from .views import * 


urlpatterns = [
    path('', home, name= "home"), 
    path('articulos/', articulos, name= "articulos"),    
    path('comentarios/', comentarios, name= "comentarios"),  
    path('acerca/', acerca, name= "acerca"),  
    path('contacto/', contacto, name= "contacto"),
    path('perfil/', perfil, name= "perfil"),

#--------------------------------Usuarios-----------------------------
    path('usuarios/', UsuarioList.as_view(), name= "usuarios"),
    path('crear_usuarios/', UsuarioCreate.as_view(), name= "crear_usuarios"),
    path('actualizar_usuarios/<int:pk>/', UsuarioUpdate.as_view(), name= 'actualizar_usuarios'),
    path('borrar_usuarios/<int:pk>/', UsuarioDelete.as_view(), name= 'borrar_usuarios'),



    
    #-------------------------------Forms--------------------------
    path('articulosForm/', createArticulo, name= "articulosForm"),
    path('actualizar_articulos/<id_articulo>/', updateArticulos, name= "actualizarArticulos"),
    path('borrar_articulos/<id_articulo>/', deleteArticulos, name= "borrarArticulos"),
    path('ver_articulo/<id_articulo>/', verArticulo, name= "verArticulo"),
    

    path('buscar/', buscar, name= "buscar"),
    path('buscarArticulos/', buscarArticulos, name= "buscarArticulos"),    

#--------------------------------Login,Logout,Registarse-----------------------------
    path('login/', login_request, name= "login"),  
    path('registro/', register, name= "registro"), 
    path('logout/', custom_logout, name= "logout"),
         
      
]            






