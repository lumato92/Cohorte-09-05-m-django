from django.shortcuts import render
from health.models import Health, Doctor, Turno
from health.forms import DoctorModalForm, TurnoForm
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from datetime import date
# Create your views here.

#Testeo Modals
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy




def mainPage(request):
    user = request.user
    userHealth = Health.objects.get(user = user)
    doctors = Doctor.objects.filter(user=user)
    turnos=Turno.objects.filter(user=user)
    serialized_data = serialize("json", turnos, use_natural_foreign_keys=True)
    serialized_data = json.loads(serialized_data)
    
    context = {
        'user' : user,
        'health': userHealth,
        'age' : calculate_age(user.dob),
        "doctors":doctors,
        "turnos":serialized_data,
    }
    return render(request, 'dashboard/main.html', context)




def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def test(request):

    return render(request,'dashboard/test.html')

#Testeo Modals

class DoctorCreateView(BSModalCreateView):
    template_name = 'health/doctorformtest.html'
    form_class = DoctorModalForm
    success_message = 'Doctor agregado'
    success_url = reverse_lazy('mainPage')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@login_required
def newTurno(request):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return HttpResponse("OK")
    return HttpResponse("ERROR")