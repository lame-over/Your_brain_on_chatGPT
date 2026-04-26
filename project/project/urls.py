from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('mainpage.urls')),
    path('quest/', include('questions.urls')),
] + i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name = 'javascript_catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
