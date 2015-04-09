from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from bookmarks.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns = patterns('', 
	url(r'^$', main_page),
)