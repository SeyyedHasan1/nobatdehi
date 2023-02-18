from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm
# Create your views here.

def reserve(request):
    reservation = Reservation.objects.all()
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'reservation' : reservation,
    }
    return render(request,'reservation/reserve.html',context)