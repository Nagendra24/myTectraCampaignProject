from django.conf.urls import url
from groupApp import views

urlpatterns = [
    url('^home_page/group$',views.group_page,name='group_page'),
    ]