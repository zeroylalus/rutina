
from django import forms


class tf_cuerpo (forms.Form):

    cuerpo = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: PARTE DEL CUERPO'
    }))


class tf_ejercicio (forms.Form):

    cuerpo = forms.IntegerField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: # PARTE DE CUERPO'
    }))

    ejercicio = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: EJERCICIO'
    }))

    posicion = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: POSICIÓN'
    }))

    tipo = forms.CharField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: TIPO'
    }))

    repeticiones = forms.IntegerField(label='',widget=forms.TextInput(attrs={
        'class':'form',
        'style': 'width: 900px;',
        'placeholder': 'ESCRIBE: # REPETICIONES'
    }))