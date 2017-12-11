from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.drive, name='drive'),
    url(r'^profiles/edit/', views.activateDriver, name='activatedriver'),
    url(r'^pickupoint/$', views.create_pickupoints, name='pickupoint'),
    url(r'^travelplan/$', views.create_travelplan, name='create_travelplan'),
    url(r'^travelplan/edit/(\d+)$',
        views.update_travelplan, name='update_travelplan'),
    url(r'^travelplan/history/(\d+)$',
        views.travelplan_history, name='travelplan_history'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
