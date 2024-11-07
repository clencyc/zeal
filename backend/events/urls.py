# urls.py
from django.urls import path
from . import views
from .views import EventListView, EventDetailView

urlpatterns = [
    path('', views.event_list_view, name='events'),
    # path('api/events', EventListView.as_view(), name='api-event-list'),
    # path('api/eventsdet/', EventDetailView.as_view(), name='api-event-details')
]