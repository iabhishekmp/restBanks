from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import detailView, listView

urlpatterns = {
    url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', detailView),
    url(r'^branches/(?P<city>.*)/(?P<bank>.*)$', listView)
}

urlpatterns = format_suffix_patterns(urlpatterns)