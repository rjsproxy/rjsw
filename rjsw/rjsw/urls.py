from django.conf.urls import include, url
from django.contrib import admin

from blog.views import BaseView

urlpatterns = [
    # url(r'^django/', include(admin.site.urls)),
    url(r'^$', BaseView),
]

