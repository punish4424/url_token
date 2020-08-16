from django.urls import path

from url_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<token>/', views.URLView.as_view(), name='index')
]
