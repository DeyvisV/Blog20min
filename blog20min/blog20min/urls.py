from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import IndexView, EntryDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog20min.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),

    url(r'^$', IndexView.as_view()),
    url(r'^entry/(?P<slug>[-\w]+)/$', EntryDetailView.as_view()),
)
