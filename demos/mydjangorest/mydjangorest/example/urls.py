from django.conf.urls import url
from example import views

urlpatterns = [
    url(r'^example/$', views.SnippetList.as_view()),
    url(r'^example/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
]