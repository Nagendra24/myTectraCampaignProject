from django.conf.urls import url
from users import views

urlpatterns = [
    url('^user_login$',views.user_login,name='userLogin'),
    url('^home_page$',views.home_page,name='homePage'),
    url('^home_page/user$',views.user_page,name='user_page'),
    url('^home_page/group$',views.group_page,name='group_page'),
    url('^home_page/user/edit/(?P<pk>[0-9]+)$',views.user_edit,name='group_page'),
    url(r'^home_page/user/delete/(?P<pk>[0-9]+)$', views.delete, name="delete"),
    url(r'^log_out$',views.logOut,name="LogOut"),
   ]