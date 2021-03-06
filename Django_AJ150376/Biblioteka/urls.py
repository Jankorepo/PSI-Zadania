

from django.urls import path
from . import views
urlpatterns = [
        path('ksiazki', views.KsiazkaList.as_view(), name=views.KsiazkaList.name),
        path('ksiazki/<int:pk>/', views.KsiazkaDetail.as_view(), name=views.KsiazkaDetail.name),
        path('gatunki', views.GatunekList.as_view(), name=views.GatunekList.name),
        path('gatunki/<int:pk>', views.GatunekDetail.as_view(), name=views.GatunekDetail.name),
        path('czytelnicy', views.CzytelnikList.as_view(), name=views.CzytelnikList.name),
        path('czytelnicy/<int:pk>/', views.CzytelnikDetail.as_view(), name=views.CzytelnikDetail.name),
        path('wypozyczenia', views.AktualneWypozyczeniaList.as_view(), name=views.AktualneWypozyczeniaList.name),
        path('wypozyczenia/<int:pk>/', views.AktualneWypozyczeniaDetail.as_view(),
             name=views.AktualneWypozyczeniaDetail.name),
        path('historia', views.HistoriaWypozyczenList.as_view(), name=views.HistoriaWypozyczenList.name),
        path('historia/<int:pk>/', views.HistoriaWypozyczenDetail.as_view(), name=views.HistoriaWypozyczenDetail.name),
        path('uzytkownicy', views.PracownikList.as_view(), name=views.PracownikList.name),
        path('uzytkownicy/<int:pk>/', views.PracownikDetail.as_view(), name=views.PracownikDetail.name),
        path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]

