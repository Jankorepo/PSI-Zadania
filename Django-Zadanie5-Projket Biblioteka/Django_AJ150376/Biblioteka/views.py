from .models import Ksiazka, Czytelnik, PunktOdbiorczy, WypozyczoneKsiazki, HistoriaWypozyczen
from .serializers import KsiazkaSerializer, CzytelnikSerializer, PunktOdbiorczySerializer
from .serializers import HistoriaWypozyczenSerializer, WypozyczoneKsiazkiSerializer
from rest_framework import generics

class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer

class CzytelnikList(generics.ListCreateAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer
class CzytelnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer

class PunktOdbiorczyList(generics.ListCreateAPIView):
    queryset = PunktOdbiorczy.objects.all()
    serializer_class = PunktOdbiorczySerializer
class PunktOdbiorczyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PunktOdbiorczy.objects.all()
    serializer_class = PunktOdbiorczySerializer

class WypozyczoneKsiazkiList(generics.ListCreateAPIView):
    queryset = WypozyczoneKsiazki.objects.all()
    serializer_class = WypozyczoneKsiazkiSerializer
class WypozyczoneKsiazkiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WypozyczoneKsiazki.objects.all()
    serializer_class = WypozyczoneKsiazkiSerializer

class HistoriaWypozyczenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer
