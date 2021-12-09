from django.urls import path
from .views import menu_invoices, buy_invoiceslist, sell_invoiceslist, new_invoicesell, edit_invoicesell

app_name = 'invoices'
urlpatterns = [
    path("invoicesmenu/", menu_invoices, name="menu_invoices"),
    path("invoicesbuylist/", buy_invoiceslist, name="buy_invoices_list"),
    path("invoicesselllist/", sell_invoiceslist, name="sell_invoices_list"),
    path("newinvoicessel/", new_invoicesell, name="new_invoicesell"),
    path("editinvoicessel/<int:id>", edit_invoicesell, name="edit_invoicesell"),

]
