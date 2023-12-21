from django.contrib import admin
from django.urls import path
from paraphrase_translator_app.views import home, translate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #path('paraphrase/', paraphrase, name='paraphrase'),
    path('translate/', translate, name='translate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)