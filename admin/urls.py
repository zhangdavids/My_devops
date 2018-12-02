
from django.conf.urls import include, url
from django.contrib import admin

import xadmin


urlpatterns = [
    # url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^user/', include('users.urls', namespace='users')),
    url(r'^', include('detail.urls', namespace='detail')),
    url(r'^record/', include('operations.urls', namespace='operations')),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^ansible/', include('taskdo.urls', namespace='taskdo')),
]
