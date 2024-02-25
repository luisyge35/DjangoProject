from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('book/', book, name="book"),
    path('reservations/', reservations, name="reservations"),
    path('menu/', menuView.as_view(), name="menu"),
    path('menu_item/<int:pk>/', singleMenuView.as_view(), name="menu_item"),  
    path('booking/', bookingView.as_view(), name='bookings'),
    path('restaurant/booking/', include(router.urls)),
]