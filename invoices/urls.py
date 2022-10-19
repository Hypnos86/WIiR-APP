from django.urls import path
from .views import menu_invoices, buy_invoices_list, buy_invoices_list_archive, new_invoice_buy, sell_invoices_list,\
    sell_invoices_list_archive, new_invoice_sell, edit_invoice_sell, edit_invoice_sell_archive,edit_invoice_buy, make_verification, show_info_buy, \
    show_info_sell, corrective_note_list, corrective_note_list_archive, show_info_note, new_note, \
    edit_note, edit_note_archive, make_pdf_from_invoices_sell, add_items_invoice_buy, delete_items_invoice_buy, delete_invoice_buy

app_name = "invoices"
urlpatterns = [
    path("menu/", menu_invoices, name="menu_invoices"),
    path("buy_list/", buy_invoices_list, name="buy_invoices_list"),
    path("info_buy/<int:id>", show_info_buy, name="show_info_buy"),
    path("archive_buy/<int:year>", buy_invoices_list_archive, name="buy_invoices_list_archive"),
    path("new_invoice_buy/", new_invoice_buy, name="new_invoice_buy"),
    path("edit_invoice_buy/<int:id>", edit_invoice_buy, name="edit_invoice_buy"),
    path("delete_invoice_by/<int:id>", delete_invoice_buy, name="delete_invoice_buy"),
    path("add_invoice_item/<int:id>", add_items_invoice_buy, name="add_items_invoice_buy"),
    path("delete_item/<int:id>/<int:invoice_id>", delete_items_invoice_buy, name="delete_items_invoice_buy"),
    path("ewidencja_fv_sprzedaz/", sell_invoices_list, name="sell_invoices_list"),
    path("info_sell/<int:id>/", show_info_sell, name="show_info_sell"),
    path("archive_sell/<int:year>/", sell_invoices_list_archive, name="sell_invoices_list_archive"),
    path("new_invoice_sell/", new_invoice_sell, name="new_invoice_sell"),
    path("edit_invoice_sell/<int:id>/", edit_invoice_sell, name="edit_invoice_sell"),
    path("edit_invoice_sell_archiwe/<int:id>", edit_invoice_sell_archive, name="edit_invoice_sell_archive"),
    path("trezor/", make_verification, name="make_verification"),
    path("ewidencja_not_ksiegowych/", corrective_note_list, name="corrective_note_list"),
    path("info_note/<int:id>/", show_info_note, name="show_info_note"),
    path("ewidencja_not_archiwum/<int:year>", corrective_note_list_archive, name="corrective_note_list_archive"),
    path("nowa_nota/", new_note, name="new_note"),
    path("edycja_noty/<int:id>/", edit_note, name="edit_note"),
    path("edycja_noty_archiwum/<int:id>/", edit_note_archive, name="edit_note_archive"),
    path("create_pdf", make_pdf_from_invoices_sell, name="make_pdf_from_invoices_sell")
]
