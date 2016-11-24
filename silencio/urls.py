from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
]
