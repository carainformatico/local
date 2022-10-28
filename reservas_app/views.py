from django.shortcuts import render , redirect
from reservas_app.models import reserva
from reservas_app.forms import formreservas
# Create your views here.

def index(request):
    return render(request, 'index.html')

def listareservas(request):
    reservas = reserva.objects.all()
    data = {'reservas' : reservas}
    return render(request , 'reservas.html' , data)

def agregarreservas(request):
    form = formreservas()
    if request.method == 'POST':
        form = formreservas(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreservas.html', data)

def eliminarreservas(request, id):
    res = reserva.objects.get(id = id)
    res.delete()
    return redirect('/reservas')

def actualizarreservas(request, id):
    res = reserva.objects.get(id = id)
    form = formreservas(instance=res)
    if request.method == 'POST':
        form = formreservas(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreservas.html', data)