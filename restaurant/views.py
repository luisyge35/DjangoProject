# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import *
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.viewsets import * 
from .serializers import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    booking_json = "serializers.serialize('json', bookings)"
    return HttpResponse(booking_json, content_type='application/json')

class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = bookingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data})
        
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
class menuView(ListCreateAPIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = menuSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success", "data" : serializer.data})

class singleMenuView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = menuSerializer
