from django.contrib import admin
from django.urls import path, include
from . import views  # Ensure you have views imported if you are using them

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
]