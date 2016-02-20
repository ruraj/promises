from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views.promise import PromiseUserList

urlpatterns = [
    url(r'^promiseuser/$', PromiseUserList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)