from django.conf.urls import url

from . import views

app_name = 'sender'

urlpatterns = [
    url(r'^tracking/', views.tracking_mail, name='tracking_mail'),
]