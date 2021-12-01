from django.urls import path
from .views import menu_invoices

app_name = 'invoices'
urlpatterns = [
    path("invoicesmenu.html", menu_invoices, name="menu_invoices"),

]
