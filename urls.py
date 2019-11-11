from core import views

urlpatterns = [
    ...
    url(r'^api/hello/$', views.hello, name='hello'),
]
