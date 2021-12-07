from django.urls import path
from .views import menu_invoices, buy_invoiceslist, sell_invoiceslist

app_name = 'invoices'
urlpatterns = [
    path("invoicesmenu/", menu_invoices, name="menu_invoices"),
    path("invoicesbuylist/", buy_invoiceslist, name="buy_invoices_list"),
    path("invoicesselllist/", sell_invoiceslist, name="sell_invoices_list"),

]
