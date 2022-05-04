from django.urls import path
from .views import menu_invoices, buy_invoiceslist, sell_invoiceslist, new_invoicesell, edit_invoicesell

app_name = 'invoices'
urlpatterns = [
    path("ewidencja_fv/", menu_invoices, name="menu_invoices"),
    path("ewidencja_fv_wydatek/", buy_invoiceslist, name="buy_invoices_list"),
    path("ewidencja_fv_sprzedaz/", sell_invoiceslist, name="sell_invoices_list"),
    path("nowa_fv_sprzedaz/", new_invoicesell, name="new_invoicesell"),
    path("edycja_fv_sprzedaz/<int:id>", edit_invoicesell, name="edit_invoicesell"),

]
