from django.urls import path
from .views import menu_invoices, buy_invoices, sell_invoices

app_name = 'invoices'
urlpatterns = [
    path("invoicesmenu.html", menu_invoices, name="menu_invoices"),
    path("invoicesbuy.html", buy_invoices, name="buy_invoices"),
    path("invoicessell.html", sell_invoices, name="sell_invoices"),

]
