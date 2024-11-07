from django.urls import path
from . import views

urlpatterns = [
    path('book-ticket/<int:event_id>/', views.ticket_booking_view, name='ticket-booking'),
    path('booking-success/', views.booking_success, name='booking-success'),
]
