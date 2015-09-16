from django.conf.urls import include, url

urlpatterns = [
    url(r'^/?', "authentication.views.create_user", name="create"),
]
