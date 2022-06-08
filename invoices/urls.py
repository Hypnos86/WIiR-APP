from django.urls import path
from .views import menu_invoices, buy_invoices_list, new_invoice_buy, sell_invoices_list, new_invoice_sell, \
    edit_invoice_sell, edit_invoice_buy, make_verification, show_info_buy, show_info_sell

app_name = 'invoices'
urlpatterns = [
    path("ewidencja_fv/", menu_invoices, name="menu_invoices"),
    path("ewidencja_fv_wydatek/", buy_invoices_list, name="buy_invoices_list"),
    path('info_buy/<int:id>', show_info_buy, name='show_info_buy'),
    path("nowa_fv_wydatek/", new_invoice_buy, name="new_invoice_buy"),
    path("edycja_fv_kupno/<int:id>", edit_invoice_buy, name='edit_invoice_buy'),
    path("ewidencja_fv_sprzedaz/", sell_invoices_list, name="sell_invoices_list"),
    path("info_sell/<int:id>", show_info_sell, name="show_info_sell"),
    path("nowa_fv_sprzedaz/", new_invoice_sell, name="new_invoice_sell"),
    path("edycja_fv_sprzedaz/<int:id>", edit_invoice_sell, name="edit_invoice_sell"),
    path("weryfikacja_trezora", make_verification, name='make_verification')
]
