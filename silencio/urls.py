from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    url(r'^post/$', views.post_record, name='post_data'),
    url(r'^get_csrf/$', views.get_csrf_token, name='get_csrf'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
]
