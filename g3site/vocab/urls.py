from django.urls import path

from . import views

app_name='vocab'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('addWord/',views.addWordView, name='addWord'),
    path('addWord/submit/',views.submit,name='submit'),
]