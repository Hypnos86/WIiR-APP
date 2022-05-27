from django.urls import path
from .views import menu_invoices, buy_invoices_list, new_invoice_buy, sell_invoices_list, new_invoice_sell, \
    edit_invoice_sell, make_verification

app_name = 'invoices'
urlpatterns = [
    path("ewidencja_fv/", menu_invoices, name="menu_invoices"),
    path("ewidencja_fv_wydatek/", buy_invoices_list, name="buy_invoices_list"),
    path("nowa_fv_wydatek/", new_invoice_buy, name="new_invoice_buy"),
    path("ewidencja_fv_sprzedaz/", sell_invoices_list, name="sell_invoices_list"),
    path("nowa_fv_sprzedaz/", new_invoice_sell, name="new_invoice_sell"),
    path("edycja_fv_sprzedaz/<int:id>", edit_invoice_sell, name="edit_invoice_sell"),
    path('weryfikacja_trezora', make_verification, name='make_verification')
]
