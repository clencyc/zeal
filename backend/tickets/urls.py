from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter
from .views import TicketPurchaseView



urlpatterns = [
    # path('api/', include(router.urls)),
    path('', views.ticket_list, name='ticket_list'),
]
