from django.conf.urls import url

from threads.views import CreateThreadView, DetailThreadView, ListThreadView

app_name = 'threads'
urlpatterns = [
    url(r'create/$', CreateThreadView.as_view(), name="create"),
    url(r'(?P<pk>[0-9]+)/$', DetailThreadView.as_view(), name="detail"),
    url(r'list/all/$', ListThreadView.as_view(), name="listall"),
    url(r'list/(?P<author>[a-zA-Z]+)/$',
        ListThreadView.as_view(), name="listmine")
]
