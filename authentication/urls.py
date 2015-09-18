from django.conf.urls import include, url
from authentication import views

urlpatterns = [
    url(r'^$', "authentication.views.create_user", name="create"),
    url(r'user/(?P<pk>[\w]+)?$', views.UserView.as_view(), name="user"),
]
