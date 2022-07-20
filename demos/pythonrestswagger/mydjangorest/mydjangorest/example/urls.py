from django.conf.urls import url
from example import views
from example.views import schema_view

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^example/$', views.SnippetList.as_view()),
    url(r'^example/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view()),
]