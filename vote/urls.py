from django.urls import path

from . import views

app_name = 'vote'

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/<int:question_id>/', views.vote, name= 'vote'),
    path('results/<int:question_id>/', views.results, name= 'results'),
    path('resultsdata/<str:obj>/', views.resultsData, name= 'resultsdata'),
]
