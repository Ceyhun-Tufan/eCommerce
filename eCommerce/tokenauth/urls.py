from django.urls import path 
from tokenauth.views import CustomerRegistrationView,LoginView

urlpatterns = [
    path('register/', CustomerRegistrationView.as_view()),
    path('login/',LoginView.as_view())
]