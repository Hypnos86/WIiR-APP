from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('units/', include('units.urls')),
                  path('investments/', include('investments.urls')),
                  path('contracts/', include('contracts.urls')),
                  path('contractors/', include('contractors.urls')),
                  path('invoices/', include('invoices.urls')),
                  path('permanentmanagement/', include('permanentmanagement.urls')),
                  path('listregister/', include('listregister.urls')),
                  path('cpv/', include('cpvdict.urls')),
                  path('gallery/', include('gallery.urls')),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path('', include('main.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
