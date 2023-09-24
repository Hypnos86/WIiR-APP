from django.urls import path, re_path
from .views import MenuInvoicesView, BuyInvoicesListView, BuyInvoicesListArchiveView, NewInvoiceBuyView, \
    SellInvoicesListView, SellInvoicesListArchiveView, NewInvoiceSellView, EditInvoiceSellView, \
    EditInvoiceSellArchiveView, EditInvoiceBuyView, \
    MakeVerificationView, ShowInfoBuyView, ShowInfoSellView, CorrectiveNoteListView, CorrectiveNoteListArchiveView, \
    ShowCorrectiveNoteInfoView, CorrectiveNoteCreateView, CorrectiveNoteUpdateView, EditNoteArchiveView, \
    MakePDFFromInvoicesSellView, AddItemsInvoiceBuyView, \
    DeleteItemsInvoiceBuyView, \
    DeleteInvoiceBuyView

app_name = "invoices"
urlpatterns = [
    path("menu/", MenuInvoicesView.as_view(), name="menu_invoices"),
    # Wydatki
    path("buyList/", BuyInvoicesListView.as_view(), name="buy_invoices_list"),
    re_path("infoBuy/(?P<id>\d+)/$", ShowInfoBuyView.as_view(), name="show_info_buy"),
    re_path("archiveBuy/(?P<year>[0-9]{4})/$", BuyInvoicesListArchiveView.as_view(), name="buy_invoices_list_archive"),
    path("newInvoice_buy/", NewInvoiceBuyView.as_view(), name="new_invoice_buy"),
    re_path("editInvoice_buy/(?P<id>\d+)/$", EditInvoiceBuyView.as_view(), name="edit_invoice_buy"),
    re_path("deleteInvoice_by/(?P<id>\d+)/$", DeleteInvoiceBuyView.as_view(), name="delete_invoice_buy"),
    re_path("addInvoiceItem/(?P<id>\d+)/$", AddItemsInvoiceBuyView.as_view(), name="add_items_invoice_buy"),
    re_path("deleteItem/(?P<id>\d+)/(?P<invoice_id>\d+)/$", DeleteItemsInvoiceBuyView.as_view(),
            name="delete_items_invoice_buy"),
    # Sprzedaż
    path("recordFvSell/", SellInvoicesListView.as_view(), name="sell_invoices_list"),
    re_path("infoSell/(?P<id>\d+)/$", ShowInfoSellView.as_view(), name="show_info_sell"),
    re_path("archiveSell/(?P<year>[0-9]{4})/$", SellInvoicesListArchiveView.as_view(),
            name="sell_invoices_list_archive"),
    path("newInvoiceSell/", NewInvoiceSellView.as_view(), name="new_invoice_sell"),
    re_path("editInvoiceSell/(?P<id>\d+)/$", EditInvoiceSellView.as_view(), name="edit_invoice_sell"),
    re_path("editInvoiceSellArchiwe/(?P<id>\d+)/$", EditInvoiceSellArchiveView.as_view(),
            name="edit_invoice_sell_archive"),
    path("trezor/", MakeVerificationView.as_view(), name="make_verification"),
    # Noty księgowe
    path("recordAccountingNote/", CorrectiveNoteListView.as_view(), name="corrective_note_list"),
    re_path("infoNote/(?P<id>\d+)/$", ShowCorrectiveNoteInfoView.as_view(), name="show_info_note"),
    re_path("recordAccountingNoteArchive/(?P<year>[0-9]{4})/$", CorrectiveNoteListArchiveView.as_view(),
            name="corrective_note_list_archive"),
    path("newAccountingNote/", CorrectiveNoteCreateView.as_view(), name="new_note"),
    re_path("editAccountingNote/(?P<id>\d+)/$", CorrectiveNoteUpdateView.as_view(), name="edit_note"),
    re_path("editAccountingNoteArchive(?P<id>\d+)/$", EditNoteArchiveView.as_view(), name="edit_note_archive"),
    path("create_pdf/<int:year>/ ", MakePDFFromInvoicesSellView.as_view(), name="make_pdf_from_invoices_sell")
]
