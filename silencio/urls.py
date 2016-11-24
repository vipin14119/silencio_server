from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    url(r'^post/$', views.post_data, name='post_data'),
]
