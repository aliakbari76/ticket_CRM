from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Ticket 
from .serializer import TicketSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    tickets = Ticket.objects.all()
    #check is user is logging in : 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username= username , password= password)
        if user is not None:
            login(request,user)
            messages.success(request, "you have been logged in")
            return redirect('home')
        else : 
            messages.success(request,"There was an error in Logging in! please try again!")
            return redirect('home')
    return render(request, 'home.html', {'tickets':tickets })

def ecuprog_tickets(request):
    tickets = Ticket.objects.filter(device='ECUProg2')
    #check is user is logging in : 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username= username , password= password)
        if user is not None:
            login(request,user)
            messages.success(request, "you have been logged in")
            return redirect('home')
        else : 
            messages.success(request,"There was an error in Logging in! please try again!")
            return redirect('home')
    return render(request, 'home.html', {'tickets':tickets })

def negaremap_tickets(request):
    tickets = Ticket.objects.filter(device='Negaremap')
    #check is user is logging in : 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username= username , password= password)
        if user is not None:
            login(request,user)
            messages.success(request, "you have been logged in")
            return redirect('home')
        else : 
            messages.success(request,"There was an error in Logging in! please try again!")
            return redirect('home')
    return render(request, 'home.html', {'tickets':tickets })

def logout_user(request):
    logout(request)
    messages.success(request , "you have been logged out!")
    return redirect('home')


@api_view(['GET'])
def getData(request):
    app = Ticket.objects.all()
    serializer = TicketSerializer(app , many = True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    file = request.FILES.get('file')
    data = {
        'name':request.data.get('name'),
        'device':request.data.get('device'),
        'serial_number' : request.data.get('serial_number'),
        'phone' : request.data.get('phone'),
        'description': request.data.get('description'),
        'file':file
    }
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
    
    
def download_file(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    file_path = ticket.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response

def delete_ticket(request , ticket_id):
    ticket = get_object_or_404(Ticket , id = ticket_id)
    ticket.delete()
    messages.success(request , "ticket has been deleted!")
    return redirect('home')