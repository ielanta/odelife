from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
# from django.views.defaults import page_not_found, server_error


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^aromas/', include('aroma.urls')),
    url(r'^me/', include('activity.urls')),
    url(r'^', include('main.urls')),
    # url(r'^404/$', page_not_found, kwargs={'exception': Exception("Page not Found")}),
    # url(r'^500/$', server_error),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
