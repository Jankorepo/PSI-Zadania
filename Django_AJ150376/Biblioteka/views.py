from .models import Ksiazka, Czytelnik, HistoriaWypozyczen, AktualneWypozyczenia, Gatunek
from .serializers import KsiazkaSerializer, CzytelnikSerializer, HistoriaWypozyczenSerializer,\
    AktualneWypozyczeniaSerializer, GatunekSerializer, PracownikSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import DateFilter,  FilterSet
from django.contrib.auth.models import User
from rest_framework import permissions

class KsiazkaFilter(FilterSet):
    najnowszeKsiazki = DateFilter(field_name="data_wydania", lookup_expr='gte')
    najstarszeKsiazki = DateFilter(field_name="data_wydania", lookup_expr='lte')
    class Meta:
        model = Ksiazka
        fields = ['najnowszeKsiazki','najstarszeKsiazki']

class GatunekList(generics.ListCreateAPIView):
    queryset = Gatunek.objects.all()
    serializer_class = GatunekSerializer
    ordering_fields = ['kategoria', 'ksiazki']
    name='gatunek-list'
    permission_classes = [permissions.IsAuthenticated]
class GatunekDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gatunek.objects.all()
    serializer_class = GatunekSerializer
    name = 'gatunek-detail'
    permission_classes = [permissions.IsAuthenticated]

class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name='ksiazka-list'
    ordering_fields = ['tytul', 'autor', 'idKsiazka']
    filter_class=KsiazkaFilter
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name='ksiazka-detail'
    permission_classes = [permissions.IsAuthenticated]

class CzytelnikList(generics.ListCreateAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer
    name = 'czytelnik-list'
    ordering_fields = ['imie', 'nazwisko', 'idCzytelnik']
    search_fields = ['imie', 'nazwisko', 'idCzytelnik']
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
class CzytelnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer
    name = 'czytelnik-detail'
    permission_classes = [permissions.IsAuthenticated]

class AktualneWypozyczeniaList(generics.ListCreateAPIView):
    queryset = AktualneWypozyczenia.objects.all()
    serializer_class = AktualneWypozyczeniaSerializer
    name = 'aktualnewypozyczenia-list'
    filter_fields = ['czytelnik_id','ksiazka_id']
    ordering_fields = ['data_wypozyczenia', 'idWypozyczenia', 'ksiazka_id']
class AktualneWypozyczeniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AktualneWypozyczenia.objects.all()
    serializer_class = AktualneWypozyczeniaSerializer
    name = 'aktualnewypozyczenia-detail'
    permission_classes = [permissions.IsAuthenticated]

class HistoriaWypozyczenList(generics.ListCreateAPIView):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer
    name = 'historiawypożyczeń-list'
    ordering_fields = ['data_wypozyczenia','data_zwrotu', 'idWypozyczenia']
    permission_classes = [permissions.IsAuthenticated]
class HistoriaWypozyczenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer
    name = 'historiawypożyczeń-detail'
    permission_classes = [permissions.IsAuthenticated]

class PracownikList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PracownikSerializer
    name = 'uzytkownik-list'
    ordering_fields = ['username']
    permission_classes = [permissions.IsAdminUser]
class PracownikDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PracownikSerializer
    name = 'uzytkownik-detail'
    permission_classes = [permissions.IsAdminUser]

class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get (self, request, *args, **kwargs):
        return Response ({'Ksiażki': reverse(KsiazkaList.name, request=request),
                          'Gatunki': reverse(GatunekList.name, request=request),
                          'Czytelnicy': reverse(CzytelnikList.name, request=request),
                          'Wypożycz Książkę': reverse(AktualneWypozyczeniaList.name, request=request),
                          'Pracownicy': reverse(PracownikList.name, request=request)
                          })