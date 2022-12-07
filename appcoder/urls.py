from django.contrib import admin
from django.urls import path
from appcoder.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('appcoder/admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('appcoder/inicio/', index, name='inicio'),

    path('appcoder/login/', Iniciar_Sesion, name='auth_login'),
    path('appcoder/register/', Registrar_Usuario, name='registrar_usuario'),
    path('appcoder/logout/', LogoutView.as_view(template_name='appcoder/logout.html'), name='auth_logout'),

    path('appcoder/editar_perfil/', Editar_Perfil, name='auth-perfil-editar'),
    path('appcoder/agregar_avatar/', Agregar_Avatar, name='auth-avatar'),
    
    path('appcoder/cursos/', Cursos, name='cursos'),
    path('appcoder/cursos_vista/', Vista_Cursos, name='cursos_vista'),
    path('appcoder/cursos/crear/', Creacion_Curso, name='curso_formulario'),
    path('appcoder/cursos/buscar/', Resultado_Buscar_Curso, name='curso_buscar'),
    path('appcoder/cursos/borrar/<id>/', Borrar_Curso, name='curso_borrar'),
    path('appcoder/cursos/editar/<id>/', Editar_Curso, name='curso_editar'),

    path('appcoder/estudiantes/', Estudiantes, name='estudiantes'),
    path('appcoder/estudiantes_vista/', Vista_Estudiantes, name='estudiantes_vista'),
    path('appcoder/estudiantes/crear/', Creacion_Estudiantes, name='estudiantes_formulario'),
    path('appcoder/estudiantes/buscar/', Resultado_Buscar_Estudiante, name='estudiante_buscar'),
    path('appcoder/estudiantes/borrar/<id>/', Borrar_Estudiante, name='estudiantes_borrar'),
    path('appcoder/estudiantes/editar/<id>/', Editar_Estudiante, name='estudiantes_editar'),

    path('appcoder/profesores/', Profesores, name='profesores'),
    path('appcoder/profesores_vista/', Vista_Profesores, name='profesores_vista'),
    path('appcoder/profesores/crear/', Creacion_Profesores, name='profesores_formulario'),
    path('appcoder/profesores/buscar/', Resultado_Buscar_Profesor, name='profesor_buscar'),
    path('appcoder/profesores/borrar/<id>/', Borrar_Profesor, name='profesores_borrar'),
    path('appcoder/profesores/editar/<id>/', Editar_Profesor, name='profesores_editar'),

    path('appcoder/entregables/', EntregablesList.as_view(), name='entregables'),
    path('appcoder/entregables/detalle/<pk>/', EntregableDetail.as_view(), name='entregables_detail'),
    path('appcoder/entregables/crear/', EntregableCreate.as_view(), name='entregables_create'),
    path('appcoder/entregables/actualizar/<pk>/', EntregableUpdate.as_view(), name='entregables_update'),
    path('appcoder/entregables/borrar/<pk>/', EntregableDelete.as_view(), name='entregables_delete'),
    ]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)