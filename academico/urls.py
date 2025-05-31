from django.urls import path
from .views import CrearAsignaturaView, CrearCalificacionView, eliminar_calificacion  # Agregar la nueva vista
from . import views 


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lista_calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
    path('calificaciones_estudiante/', views.calificaciones_estudiante, name='calificaciones_estudiante'),
    # Recuperación de contraseña
    path('recuperar-contrasena/', views.recuperar_contrasena_usuario, name='recuperar_contrasena_usuario'),
    path('recuperar-contrasena/pregunta/', views.recuperar_contrasena_pregunta, name='recuperar_contrasena_pregunta'),
    path('recuperar-contrasena/reset/', views.recuperar_contrasena_reset, name='recuperar_contrasena_reset'),
    # Ruta para configurar la seguridad
    path('configurar-seguridad/', views.configurar_seguridad, name='configurar_seguridad'),
    path('profesor/calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
        path('asignatura/crear/', CrearAsignaturaView.as_view(), name='crear_asignatura'),
    path('calificacion/crear/', CrearCalificacionView.as_view(), name='crear_calificacion'),
    path('informes-rendimiento/', views.informes_rendimiento, name='informes_rendimiento'), 
    path('editar-calificacion/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    # Nueva ruta para eliminar calificaciones
    path('calificacion/eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('previsualizar-informe-individual/<int:estudiante_id>/<int:periodo>/', views.previsualizar_informe_individual, name='previsualizar_informe_individual'),
]