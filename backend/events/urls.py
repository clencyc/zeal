# urls.py
from django.urls import path
from . import views
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', views.event_list_view, name='events')
]