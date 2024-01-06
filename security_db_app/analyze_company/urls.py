from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('upload_edinet', upload_Edinet, name='upload_edinet'), # DB作成のための一時的なview
    path('upload_detail', upload_detail, name='upload_detail'), # DB作成のための一時的なview
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)