from django.conf.urls import url, include 
from rest_framework.urlpatterns import format_suffix_patterns
from app.restviews import views

urlpatterns =[
	url(r'^usuarios/$', views.UserList.as_view()),
	url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)