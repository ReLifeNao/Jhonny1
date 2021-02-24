
from django.urls import path
from . import views
app_name = 'sistema'
urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.complement, name='index3'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
]