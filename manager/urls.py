from django.contrib.auth.views import LogoutView
from django.urls import path

from manager.views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about-us/', AboutUs.as_view(), name="about-us"),
    path('event-new/', EventFormView.as_view(), name='event-new'),
    path('events/', Events.as_view(), name='events'),
    path('get-contract/', Contract.as_view(), name='get-contract'),
    path('maintenance-new/', MaintenanceFormView.as_view(), name='maintenance-new'),
    path('maintenance-requests/', MaintenanceRequests.as_view(), name='maintenance-requests'),
    path('maintenance-status/<int:pk>/', MaintenanceStatus.as_view(), name="maintenance-status"),

]
