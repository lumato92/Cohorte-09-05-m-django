from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from health.forms import HealthForm, RecetaForm, DoctorForm, TurnoForm
from health.models import Health,Doctor


# Create your views here.
@login_required
def healthForm(request):
    user = request.user
    try:
        if Health.objects.filter(user=user).first() is not None:
            return redirect("fichaMedica")
    except:
        print("error,healthform")

    if request.method == "POST":
        form = HealthForm(request.POST)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = HealthForm()
        doctors = Doctor.objects.filter(user=user)  
        context = {"form": form, "user": user,"doctors":doctors}
    print("flujo")
    return render(request, "health/healthform.html", context)


@login_required
def newReceta(request):

    user = request.user

    if request.method == "POST":

        user = request.user
        print(user)
        print("llego aca")

        form = RecetaForm(request.POST, request.FILES)

        print(form.is_valid())

        if form.is_valid():
            print("llego aca 3")
            form.instance.user = user
            form.save()
            return redirect("home")
    else:
        form = RecetaForm()

        context = {
            "user": user,
            "form": form,
        }

        return render(request, "health/newreceta.html", context)


@login_required
def newDoctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print("aca")
            return redirect("home")
    else:
        form = DoctorForm()

        context = {
            "form": form,
        }

        return render(request, "health/doctorform.html", context)

@login_required
def fichaMedica(request):

    user = request.user

    form = Health.objects.get(user = user)
    health=Health.objects.get(user=user)
    doctors = Doctor.objects.filter(user=user) 
    context = {
        'user': user,
        'form': form,
        'health': health,
        "doctors":doctors
    }
    if request.method == "POST":
        form = HealthForm(request.POST,instance=health)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect("home")
    return render (request,'health/healthform.html',context)

@login_required
def newTurno(request):
    user = request.user
    if request.method == "POST":
        form = TurnoForm(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("home")
    else:
        form = TurnoForm()
        doctors = Doctor.objects.filter(user=user) 
        context = {
            "form": form,
            "doctors":doctors
        }

        return render(request, "health/turnoform.html", context)
