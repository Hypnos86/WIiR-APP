from django.urls import path, re_path
from .views import menu_invoices, buy_invoices_list, buy_invoices_list_archive, new_invoice_buy, sell_invoices_list,\
    sell_invoices_list_archive, new_invoice_sell, edit_invoice_sell, edit_invoice_sell_archive,edit_invoice_buy, make_verification, show_info_buy, \
    show_info_sell, corrective_note_list, corrective_note_list_archive, show_info_note, new_note, \
    edit_note, edit_note_archive, make_pdf_from_invoices_sell, add_items_invoice_buy, delete_items_invoice_buy, delete_invoice_buy

app_name = "invoices"
urlpatterns = [
    path("menu/", menu_invoices, name="menu_invoices"),
    # Wydatki
    path("buyList/", buy_invoices_list, name="buy_invoices_list"),
    re_path("infoBuy/(?P<id>\d+)/$", show_info_buy, name="show_info_buy"),
    re_path("archiveBuy/(?P<year>[0-9]{4})/$", buy_invoices_list_archive, name="buy_invoices_list_archive"),
    path("newInvoice_buy/", new_invoice_buy, name="new_invoice_buy"),
    re_path("editInvoice_buy/(?P<id>\d+)/$", edit_invoice_buy, name="edit_invoice_buy"),
    re_path("deleteInvoice_by/(?P<id>\d+)/$", delete_invoice_buy, name="delete_invoice_buy"),
    re_path("addInvoiceItem/(?P<id>\d+)/$", add_items_invoice_buy, name="add_items_invoice_buy"),
    re_path("deleteItem/(?P<id>\d+)/(?P<invoice_id>\d+)/$", delete_items_invoice_buy, name="delete_items_invoice_buy"),
    # Sprzedaż
    path("recordFvSell/", sell_invoices_list, name="sell_invoices_list"),
    re_path("infoSell/(?P<id>\d+)/$", show_info_sell, name="show_info_sell"),
    re_path("archiveSell/(?P<year>[0-9]{4})/$", sell_invoices_list_archive, name="sell_invoices_list_archive"),
    path("newInvoiceSell/", new_invoice_sell, name="new_invoice_sell"),
    re_path("editInvoiceSell/(?P<id>\d+)/$", edit_invoice_sell, name="edit_invoice_sell"),
    re_path("editInvoiceSellArchiwe/(?P<id>\d+)/$", edit_invoice_sell_archive, name="edit_invoice_sell_archive"),
    path("trezor/", make_verification, name="make_verification"),
    # Noty księgowe
    path("recordAccountingNote/", corrective_note_list, name="corrective_note_list"),
    re_path("infoNote/(?P<id>\d+)/$", show_info_note, name="show_info_note"),
    re_path("recordAccountingNoteArchive/(?P<year>[0-9]{4})/$", corrective_note_list_archive, name="corrective_note_list_archive"),
    path("newAccountingNote/", new_note, name="new_note"),
    re_path("editAccountingNote/(?P<id>\d+)/$", edit_note, name="edit_note"),
    re_path("editAccountingNoteArchive(?P<id>\d+)/$", edit_note_archive, name="edit_note_archive"),
    path("create_pdf/<int:year>/", make_pdf_from_invoices_sell, name="make_pdf_from_invoices_sell")
]
