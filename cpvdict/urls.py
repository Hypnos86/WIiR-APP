from django.urls import path, re_path
from cpvdict.views import CpvDictionary, GenericMenu, OrderListView, ShowOrderInfo, NewOrderView, ConstructionWorksClassificationListView, \
    ShowInfoWorkObject, EditOrderView, ArchiveYearListView, OrderArchiveListView, \
    ConstructionWorksArchiveList, GenreArchiveView

app_name = 'cpvdict'
urlpatterns = [
    path('dictCPV/', CpvDictionary.as_view(), name='cpvlist'),
    path('genreTree/', GenericMenu.as_view(), name='type_expense_list'),
    path('buildingWorks/', ConstructionWorksClassificationListView.as_view(), name='type_work_list'),
    re_path('info/(?P<id>\d+)>/(?P<year>[0-9]{4})/$', ShowInfoWorkObject.as_view(), name='show_information_work_object'),
    path('orderList/', OrderListView.as_view(), name='order_list'),
    re_path('info/(?P<id>\d+)/$', ShowOrderInfo.as_view(), name='show_order_info_popup'),
    path('new_order/', NewOrderView.as_view(), name='new_order'),
    re_path('editOrder/(?P<id>\d+)/$', EditOrderView.as_view(), name='edit_order'),
    path('archiveListYear/', ArchiveYearListView.as_view(), name='make_archive_year_list'),
    re_path('archiveListOrder/(?P<year>\d+)/$', OrderArchiveListView.as_view(), name='create_order_archive'),
    re_path('archiveBuildingWorks/(?P<year>\d+)/$', ConstructionWorksArchiveList.as_view(), name='create_type_work_list_archive'),
    re_path('genreTreeArchive/(?P<year>\d+)/$', GenreArchiveView.as_view(), name='create_genre_archive')
]
