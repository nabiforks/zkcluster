from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^terminal/$', views.terminal, name='terminal'),
    url(r'^terminal/save$', views.terminal_save, name='terminal_save'),
    url(r'^terminal/add$', views.terminal_add, name='terminal_add'),
    url(r'^terminal/(?P<terminal_id>[0-9]+)/(?P<action>[\w-]+)/$', views.terminal_action, name='terminal_action'),
    url(r'^user/$', views.user, name='user'),
    url(r'^user/add/$', views.user_add, name='user_add')
]