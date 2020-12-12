

from django.urls import path
from . import views
urlpatterns = [
    path('ksiazki', views.KsiazkaList.as_view()),
    path('ksiazki/<int:pk>/', views.KsiazkaDetail.as_view()),
    path('czytelnicy', views.CzytelnikList.as_view()),
    path('czytelnicy/<int:pk>/', views.CzytelnikDetail.as_view()),
    path('punktOdbiorczy', views.PunktOdbiorczyList.as_view()),
    path('punktOdbiorczy/<int:pk>/', views.PunktOdbiorczyDetail.as_view()),
    path('wypozyczenia', views.WypozyczoneKsiazkiList.as_view()),
    path('wypozyczenia/<int:pk>/', views.WypozyczoneKsiazkiDetail.as_view()),
    path('historia', views.HistoriaWypozyczenList.as_view()),
    path('historia/<int:pk>/', views.HistoriaWypozyczenDetail.as_view()),
]

