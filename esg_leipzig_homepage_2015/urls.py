from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views import generic

from . import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^admin/',
        include(admin.site.urls)),
    url(r'^(?P<slug>\w+)/$',
        views.FlatPageView.as_view(),
        name='flatpage'),
)
