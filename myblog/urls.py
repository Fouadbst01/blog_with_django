from django.urls import path
#from myblog.views import auter_view
from myblog.views import home_view
from myblog.views import delete_blog
from myblog.views import new_blog

app_name="myblog"
urlpatterns=[
    #path('auteur/<int:id_auteur>/',auter_view,name="get_auter"),
    path('delete/<int:id_blog>',delete_blog,name='delete_blog'),
    path('save/',new_blog,name="save"),
    path('',home_view,name="home")
]