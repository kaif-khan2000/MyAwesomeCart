from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='blogHome'),
    path("blogpost_/<int:id>",views.blogpost,name='blogpost'),
    path("search/",views.search,name='search'),
]