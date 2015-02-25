from django.conf.urls import patterns, include, url
from django.contrib import admin
from dsi_2_django.views import hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dsi_2_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
)
