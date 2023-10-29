from django.shortcuts import render,redirect
from landing.models import BookNow
# Create your views here.

def home(request):
    return render(request, 'landing/index.html')

def book_now(request):
    if request.method=="GET":
        print("hi")
        return render(request,'landing/index.html')
    else:
        fcity=request.POST['fcity']
        ftcity=request.POST['ftcity']
        fdate=request.POST['fdate']
        fnumber=request.POST['fnumber']

        o=BookNow.objects.create(from_city=fcity,to_city=ftcity,d_journey=fdate,n_persons=fnumber)
        o.save()
        return redirect('/bookings')
    
def bookings(request):
    o=BookNow.objects.all()
    return render(request,'landing/booking.html',{'bookings':o})

def edit_journey(request,eid):
    o=BookNow.objects.filter(id=eid)
    if request.method=="GET":
        return render(request,'landing/editjourney.html',{'bookings':o})
    else:
        fcity=request.POST['fcity']
        ftcity=request.POST['ftcity']
        fdate=request.POST['fdate']
        fnumber=request.POST['fnumber']
        print(fcity)
        o.update(from_city=fcity,to_city=ftcity,d_journey=fdate,n_persons=fnumber)
        return redirect('/bookings')
    
def delete_journey(request,did):
    o=BookNow.objects.filter(id=did)
    o.delete()
    return redirect('/bookings')