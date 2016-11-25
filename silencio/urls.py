from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    url(r'^post/$', views.post_data, name='post_data'),
    url(r'^get_csrf/$', views.get_csrf_token, name='get_csrf'),
]
