from django.conf.urls.defaults import *
from django.conf import settings
from txts.feeds import *

feeds = {
    'blog': BlogEntries,
    'obert': OpenKnowledge,
}

urlpatterns = patterns('',
    (r'^r/', include('django.conf.urls.shortcut')),
    (r'^admin/', include('django.contrib.admin.urls')),
    #
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^photoplanet/', include('photoplanet.urls')),
    #(r'^links/', include('links.urls')),
    (r'^', include('txts.urls')),
)


if settings.LOCAL_DEV:
    urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT,
       'show_indexes': True, }),
) + urlpatterns


