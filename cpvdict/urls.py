from django.urls import path, re_path
from cpvdict.views import cpvlist, type_expense_list, order_list, show_order_info_popup, new_order, type_work_list, \
    show_information_work_object, edit_order, make_archive_year_list, create_order_archive, \
    create_type_work_list_archive, create_genre_archive

app_name = 'cpvdict'
urlpatterns = [
    path('dictCPV/', cpvlist, name='cpvlist'),
    path('genreTree/', type_expense_list, name='type_expense_list'),
    path('buildingWorks/', type_work_list, name='type_work_list'),
    re_path('info/(?P<id>\d+)>/(?P<year>[0-9]{4})/$', show_information_work_object, name='show_information_work_object'),
    path('orderList/', order_list, name='order_list'),
    re_path('info/(?P<id>\d+)/&', show_order_info_popup, name='show_order_info_popup'),
    path('new_order/', new_order, name='new_order'),
    re_path('editOrder/(?P<id>\d+)/&', edit_order, name='edit_order'),
    path('archiveListYear/', make_archive_year_list, name='make_archive_year_list'),
    re_path('archiveListOrder/(?P<year>\d+)/&', create_order_archive, name='create_order_archive'),
    re_path('archiveBuildingWorks/(?P<year>\d+)/&', create_type_work_list_archive, name='create_type_work_list_archive'),
    re_path('genreTreeArchive/(?P<year>\d+)/&', create_genre_archive, name='create_genre_archive')
]
