from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('', RedirectView.as_view(url='/services/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('services.urls')),
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)