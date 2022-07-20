from django.conf.urls import url, include
from rest_framework import routers
from example import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# these are for the user example
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# these are for the snippets
urlpatterns = [
    url(r'^', include('example.urls')),
]