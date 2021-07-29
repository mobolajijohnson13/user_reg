from django.conf.urls import url 
from apicalls import views 
 
urlpatterns = [ 
    url(r'^api/magazine$', views.magazine_list),
    url(r'^api/magazine/(?P<pk>[0-9]+)$', views.magazine_detail),
    url(r'^api/magazine/published$', views.magazine_list_published),
    url(r'^api/magazine/published_date$', views.magazine_list_published_date)
]