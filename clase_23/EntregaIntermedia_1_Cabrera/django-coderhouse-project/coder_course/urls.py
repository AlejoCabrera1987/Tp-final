from django.urls import path

from coder_course import views

urlpatterns = [
   

    path('index-2', views.index2),
    #path('cursos', views.cursos, name="Cursos"),
    path('insumos',views.insumos, name="Insumos"),
    path('tareas',views.tareas, name="Tareas"),
    path('rubros',views.rubros, name="Rubros"),
    path('familias',views.familias, name="Familias"),
    path('iniciar',views.iniciar, name="Iniciar"),
    #path('cargarFamilia',views.cargarfamilias, name="cargarFamilia"),
    path('busquedaCodigo',views.busquedaCodigo, name="BusquedaCodigo"),
    path('buscar/',views.buscar),
    path('leerFamilias',views.leerFamilias, name="leerFamilias"),
    path('familias/list',views.FamiliasList.as_view(), name ="List"),
    path(r'^(?P<pk>\d+)$',views.FamiliasDetalle.as_view(), name="Detail"),
    path(r'^nuevo$',views.FamiliasCreacion.as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$',views.FamiliasUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$',views.FamiliasDelete.as_view(), name="Delete"),
    path('login',views.login_request, name='Login'),
    #path('logout', views.logout_request, name='logout'),
    #path('register',views.register, name='register'),

]