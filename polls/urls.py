from django.urls import path
from . import views
app_name='polls'
urlpatterns=[
    path("index/",views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/result',views.results, name= 'results'),
    path('<int:pk>/vote',views.vote,name='vote'),
    
]