from django.urls import path
from . import views
urlpatterns=[
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result',views.results, name= 'result')


]