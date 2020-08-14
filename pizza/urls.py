from django.urls import path
from . import views

app_name = 'pizza'
urlpatterns = [
    path('', views.home, name='home'),
    path('payment/', views.invoice_payment, name='invoice_payment'),
    path('confirm-order/', views.confirm_order, name='confirm_order'),
]
