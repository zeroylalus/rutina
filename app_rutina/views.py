from django.shortcuts import render, redirect, get_object_or_404
from app_rutina import models
from app_rutina import rutina_forms

# Create your views here.

def f_inicio(i):
    return render(i, 'inicio.html')

def f_cuerpo(i):
    q = models.t_cuerpo.objects.all()
    return render(i, 'cuerpo/cuerpo.html',{
        'f_cuerpo': q
    })

def ff_cuerpo(i):
    if i.method == 'GET':
        return render(i, 'cuerpo/ff_cuerpo.html',
                      {'ff_cuerpo': rutina_forms.tf_cuerpo})
    else:
        models.t_cuerpo.objects.create(cuerpo = i.POST['cuerpo'])
        return redirect('f_cuerpo')
    
def d_cuerpo(i, id):
    d_cuerpo = get_object_or_404(models.t_cuerpo,id=id)
    d_ejercicio = models.t_ejercicio.objects.filter(cuerpo_id=id)
    return render(i, 'cuerpo/d_cuerpo.html',{
        'd_cuerpo':d_cuerpo,
        'd_ejercicio':d_ejercicio
    })


def f_ejercicio(i):
    q = models.t_ejercicio.objects.all()
    return render(i, 'ejercicio/ejercicio.html',{
        'f_ejercicio': q
    })


def ff_ejercicio(i):
    if i.method == 'GET':
        return render(i, 'ejercicio/ff_ejercicio.html',
                      {'ff_ejercicio': rutina_forms.tf_ejercicio})
    else:
        models.t_ejercicio.objects.create(
            repeticiones = i.POST['repeticiones'],
            ejercicio = i.POST['ejercicio'],
            posicion = i.POST['posicion'],
            cuerpo_id = i.POST['cuerpo'],
            tipo = i.POST['tipo'],
        )
        return redirect('f_cuerpo')