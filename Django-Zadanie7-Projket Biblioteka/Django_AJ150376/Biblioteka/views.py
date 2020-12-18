from .models import Ksiazka, Czytelnik, Pracownik, HistoriaWypozyczen, AktualneWypozyczenia
from .serializers import KsiazkaSerializer, CzytelnikSerializer, HistoriaWypozyczenSerializer, AktualneWypozyczeniaSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import AllValuesFilter, DateFilter, NumberFilter, FilterSet, CharFilter

class KsiazkaFilter(FilterSet):
    najnowszeKsiazki = DateFilter(field_name="data_wydania", lookup_expr='gte')
    najstarszeKsiazki = DateFilter(field_name="data_wydania", lookup_expr='lte')
    tytul = CharFilter(field_name="tytul", lookup_expr='lte')
    class Meta:
        model = Ksiazka
        fields = ['najnowszeKsiazki','najstarszeKsiazki','tytul']

class KsiazkaList(generics.ListCreateAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name='ksiazka-list'
    filter_class=KsiazkaFilter
class KsiazkaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    name='ksiazka-detail'


class CzytelnikList(generics.ListCreateAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer
    name = 'czytelnik-list'
class CzytelnikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Czytelnik.objects.all()
    serializer_class = CzytelnikSerializer
    name = 'czytelnik-detail'

class AktualneWypozyczeniaList(generics.ListCreateAPIView):
    queryset = AktualneWypozyczenia.objects.all()
    serializer_class = AktualneWypozyczeniaSerializer
    name = 'aktualneWypozyczenia-list'
class AktualneWypozyczeniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AktualneWypozyczenia.objects.all()
    serializer_class = AktualneWypozyczeniaSerializer
    name = 'aktualneWypozyczenia-detail'

class HistoriaWypozyczenList(generics.ListCreateAPIView):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer
    name = 'historiaWypożyczeń-list'
class HistoriaWypozyczenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriaWypozyczen.objects.all()
    serializer_class = HistoriaWypozyczenSerializer
    name = 'historiaWypożyczeń-detail'

class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get (self, request, *args, **kwargs):
        return Response ({'Ksiażki': reverse(KsiazkaList.name, request=request),
                          'Czytelnicy': reverse(CzytelnikList.name, request=request),
                          'AktualneWypożyczenia': reverse(AktualneWypozyczeniaList.name, request=request),
                          'HistoriaWypożyczeń': reverse(HistoriaWypozyczenList.name, request=request),
                          })