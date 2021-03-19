from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Cancha, Reserva
from .forms import ReservaForm, CustomUserCreationForm

from django.contrib.auth.forms import UserCreationForm

 
 #raul prueba registro
from django.shortcuts import render

#esto lo agrego gaby#
# lo saque raul from apps.user.forms import NewUserForm, Userprofile


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import ReservaForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def misturnos(request):
    mireserva = Reserva.objects.filter(usuario=request.user)
    data = {
        "mireserva": mireserva
    }
    return render(request, "misturnos.html", data)

def home(request):
    return render(request, "home.html")

"""@login_required()
def turnos(request):
    
    data={
        'form': ReservaForm()
    }

    if request.user.is_authenticated:
        username = request.user.username"""


@login_required
def turnos(request):

    form = ReservaForm(initial={'usuario': request.user.username})

    if request.user.is_authenticated:
        form = ReservaForm(initial={'usuario': request.user.username})
        form.full_clean() 

    if request.method=='POST':
        form=ReservaForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.usuario=request.user
            instance.save()
        return render(request, 'aviso.html')

    return render(request, 'turnos.html', {'form': form})



def registro(request):
        data = {
            "form": CustomUserCreationForm()
        }
        if request.method == "POST":
            formulario = CustomUserCreationForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                #user = authenticate (usermane=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                #login(request, user, )
                user = formulario.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                #messages.success(request, "Te has registrado correctamente")
                return redirect (to="Turnos")
            data["form"]=formulario
        return render(request, "registration/registro.html", data)


def nosotros(request):

    return render(request, "nosotros.html")



def eliminar(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect(to="Usuario")


def aviso(request):

    return render(request, "aviso.html")
    
    
def canchas(request):
    canchas = Cancha.objects.all()
    lista_canchas = {
        "canchas": canchas
     }
    return render(request, "canchas.html", lista_canchas)
    
    
    
    