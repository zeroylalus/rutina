from django.urls import path

from app_rutina import views

urlpatterns = [

    path('',views.f_inicio, name='inicio'),

    path('cuerpo/',views.f_cuerpo, name='cuerpo'),
    path('f_cuerpo/',views.ff_cuerpo, name='f_cuerpo'),
    path('d_cuerpo/<int:id>',views.d_cuerpo, name='d_cuerpo'),

    path('ejercicio',views.f_ejercicio, name='ejercicio'),
    path('f_ejercicio/',views.ff_ejercicio, name='f_ejercicio'),
    
]